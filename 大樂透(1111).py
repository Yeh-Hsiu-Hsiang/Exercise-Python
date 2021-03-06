import random
a_list = random.sample(range(1,50),7) #系統隨機取7個亂數

print(a_list)

user = input('手動1,自動為任意值') #詢問user

u_list = [] 

if user == '1':
    i = 0
    total = 1 #輸入總數

    while i < 7:  #輸入的次數<6
        user_num = input('your number {0} , or \'x\' for exit '.format(total))
        # user_num = int(user_num)
        if user_num == 'x' or user_num == 'X':
            exit() #離開程序

        try:
            user_num = int(user_num)
            if user_num < int(1) or user_num > int(49):
                print('輸入錯誤~')
                continue #跳出本次循環
  
            elif user_num in u_list:
                print('輸入重複請重新輸入')
                
            else:
                u_list.append(user_num) #把輸入的值加入陣列
                i += 1 
                total += 1
                continue  

        except ValueError:
            print('輸入錯誤')
            continue

else:
    u_list = random.sample(range(1,50),7)
    

count = 0

for j in u_list:
    if j in a_list:
        count += 1

if count == 7:
    print('恭喜中頭獎')
else:
    print('本期開獎碼是：{0}'.format(sorted(a_list)))
    print('您選的號碼是：{0}'.format(sorted(u_list)))
    print('猜中 {0} 個號碼：'.format(count))
