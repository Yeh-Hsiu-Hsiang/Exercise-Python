import socket,sys
import random
HOST = '127.0.0.1'
PORT = 7000

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creat socket

except socket.error:
    sys.stderr.write("Create failed") #create socket failed 
    sys.exit()

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #重設tcp
server.bind((HOST, PORT)) #綁定IP
server.listen(5) #監聽(最多可有()人連線)
# server.settimeout(10) #閒置時間

while True: #持續接收
    a_list = random.sample(range(0,9),4)    #隨機取亂數
    times = 0   #輸入次數
    print(a_list)

    print('Server start at: %s:%s' %(HOST, PORT))
    print('wait for connection...')

    (client, addr) = server.accept() #接收client訊息
    print('Client by ', addr)

    while True:
        user_num = client.recv(1024) #接收字元

        if not user_num:
            break
        else:
            try:
                print('Client send:' + user_num.decode("utf-8"))
                user_num = user_num.decode("utf-8")
                int(user_num)
                print(user_num)
                u_list = []
                a = 0
                b = 0

                for j  in map(int,user_num):
                    if j not in u_list:
                        u_list.append(j) #把值加入陣列
                        continue
                    else:
                        client.sendall('輸入重複'.encode('utf-8'))
                        continue

                if len(u_list) != 4:
                    continue
                else:
                    for i in range(4):
                        if u_list[i] in a_list:
                            # print(u_list[i])
                            if u_list[i] == a_list[i]:
                                a += 1
                                continue
                            else:
                                b += 1
                                continue
                    times += 1     
                    print(str(a) +'A' , str(b) +'B')        
                
                    if a == 4:
                        client.sendall('恭喜答對~  '.encode('utf-8') +
                                        '  Answer:{0}'.format(a_list).encode('utf-8') +
                                        '  共猜{0}次'.format(times).encode('utf-8'))
                        # client.sendall('恭喜答對~'.encode('utf-8'))
                        # client.sendall('Answer:{0}'.format(a_list).encode('utf-8'))
                        # client.sendall('共猜{0}次'.format(times).encode('utf-8'))

                    else:
                        client.sendall((str(a) +'A').encode('utf-8') + (str(b) +'B').encode('utf-8')) 

            except ValueError:
                client.sendall('請輸入數值'.encode('utf-8'))
                continue
    else:
        continue
# client.close()
