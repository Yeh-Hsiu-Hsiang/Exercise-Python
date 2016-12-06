import random

aa = random.sample(range(1,50),7)

print('choice or computer?')
print('input \"i\" for choice by yourself')
print('input anything else for chocie by computer')

choice = input('your choice: ')

if choice == 'i':
    choice_list = []
    count = 1

    while True:
        num = input('Input your {0} number (\"q\" for quit): '.format(count))

        if num =='q':
            exit()

        try:
            num = int(num)
            if num in choice_list:
                print('有重複喔~')
                continue
            elif num < 1 or num > 49:
                print('輸入錯誤')
                continue
        except:
            print('Please input a number')
            continue
        else:
            choice_list.append(num)
            if count == 6:
                break
            else:
                count += 1

else:
    choice_list = random.sample(range(1,50),6)

count_get = 0

for num in choice_list:
    if num in aa:
        count_get += 1

if count_get == 7 :
        print('中獎啦~')
else:
        print('猜中 {0} 個'.format(count_get))
        print('樂透的號碼:{0}'.format(aa))
        print('選的號碼是:{0}'.format(choice_list))
