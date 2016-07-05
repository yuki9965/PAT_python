__author__ = 'Yaicky'
for i in range(10000):
    temp = i
    flag = 5
    while flag:
        if (temp-1)%5==0:
            temp = (temp-1)/5*4
            flag -= 1
        else:
            break

    if flag ==0:
        print(i)
        break