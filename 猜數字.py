import random
a_list = random.sample(range(0,9),4)    #隨機取亂數

print(a_list)

user_num = 0
times = 0   #輸入次數

while(a_list != user_num):
    
    user_num = input('請輸入四個不重複的數字，按Q離開')

    if  user_num == 'q' or user_num == 'Q':
        exit()
    elif len(user_num) != 4:
        print('輸入錯誤')
        continue
    else:
        try:
            int(user_num)
            u_list = []
            a = 0
            b = 0

            for j  in map(int,user_num):
                if j not in u_list:
                    u_list.append(j) #把值加入陣列
                    continue
                else:
                    print('輸入重複')
                    break

            if len(u_list) != 4:
                continue
            else:
                for i in range(4):
                    if u_list[i] in a_list:
                        if u_list[i] == a_list[i]:
                            a += 1
                            continue
                        else:
                            b += 1
                            continue
                times += 1    
                          
                if a == 4:
                    print('恭喜答對~')
                    print('Answer：{0}'.format(a_list))
                    print('共猜{0}次 ：'.format(times))
                    break
                else:
                    print(str(a) + 'A', str(b) + 'B')
 
        except ValueError:
            print('請輸入數值')
            continue
