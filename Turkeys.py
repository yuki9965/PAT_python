__author__ = 'Yaicky'

while True:
    try:
        n = input()
        qian, bai, shi = map(int, raw_input().strip().split())
        wan, ge, price = 0, 0, 0
        flag = True
        while flag:
            for i in range(9, 0,-1):
                num = i*10000 + qian*1000 + bai*100 + shi*10 + 9
                rest = num%n
                if rest < 10:
                    price = (num - rest)/n
                    wan = i
                    ge = 9 - rest
                    flag = False
                    break
                if i == 1:
                    flag = False

        #print n, qian,bai,shi
        if price == 0:
            print '0'
        else:
            print "%d %d %d" %(wan, ge, price)
    except:
        break