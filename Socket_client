import socket,sys
HOST = '127.0.0.1'
PORT = 7000

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    sys.stderr.write("Create failed")
    sys.exit()

client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #重設tcp

try:
    client.connect((HOST,PORT))
except ConnectionRefusedError:
        sys.stderr.write("Can't connect to server, try it latter!")
        exit()
print(client.recv(1024).decode())
while True:
    
    user_num = input("請輸入四個不重複的數字，按Q離開")

    if user_num == 'q' or user_num == 'Q':
        client.send(user_num.encode('utf-8'))
        print('exit')
        break
    if len(user_num) != 4:
        print('輸入錯誤')
        continue 
    else:

        try:
            int(user_num)
            client.send(user_num.encode('utf-8')) #傳回
            user_num = client.recv(1024)
            print(user_num.decode("utf-8"))

        except ValueError:
            print('請輸入正確數值')
            continue

        if user_num.decode('utf-8') == '輸入重複':
            continue

        if len(user_num.decode('utf-8'))>5:
            break
            # exit()

# client.close()
