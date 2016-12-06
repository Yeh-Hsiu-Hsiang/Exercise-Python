import socket,sys
import random
HOST = '127.0.0.1'
PORT = 7000

while True: #持續接收
    flag = False
    a = input('請輸入數值')
    
    try:
        int(a)
        times = 0   #輸入次數
        a_list = []
        
        if len(a) != 4:
            print('輸入長度錯誤')
            continue
        
        for k in map(int,a):
            if k not in a_list:
                a_list.append(k) #把值加入陣列
                continue
            else:
                print('輸入重複')
                flag = True
                break
        if flag == True:
            continue
        while 1:
            try:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creat socket

            except socket.error:
                sys.stderr.write("Create failed") #create socket failed 
                sys.exit()

            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #重設tcp
            server.bind((HOST, PORT)) #綁定IP
            server.listen(5) #監聽(最多可有()人連線)

            print('Server start at: %s:%s' %(HOST, PORT))
            print('wait for connection...')
            (client, addr) = server.accept() #接收client訊息
            client.sendall('開始連線'.encode('utf-8'))
            print('Client by ', addr)
        
            while True:

                try:
                    user_num = client.recv(1024) #接收字元
                except ConnectionResetError:
                    print('client強制關閉')
                    exit()
                except:
                    print('time out.')
                    exit()
                
                if not user_num:
                    break
                elif user_num.decode('utf-8') == 'q' or user_num.decode('utf-8') == 'Q':
                    exit()
                else:
                    try:
                        print('Client send:' + user_num.decode("utf-8"))
                        user_num = user_num.decode("utf-8")
                        int(user_num)
                        print(user_num)
                        u_list = []
                        a = 0
                        b = 0
                            # map(int,user_num)
                        for j in map(int,user_num):
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
                                client.sendall('game over  '.encode('utf-8') +
                                     '恭喜答對~  '.encode('utf-8') +
                                        '  Answer:{0}'.format(a_list).encode('utf-8') +
                                        '  共猜{0}次'.format(times).encode('utf-8'))
                                exit()
                            else:
                                client.sendall((str(a) +'A').encode('utf-8') + (str(b) +'B').encode('utf-8')) 

                    except ValueError:
                        client.sendall('請輸入數值'.encode('utf-8'))
                        continue

    except ValueError:
        print('數值錯誤')
        continue
# client.close()
