__author__ = 'Yaicky'

while True:
    try:
        amount = map(int, raw_input().strip().split())
        rlt = []
        minIdx = 0
        count = 0
        flag = False
        for i in range(10):
            if amount[i] != 0:
                if flag == False and minIdx == 0 and i != 0 :
                    minIdx = count
                    flag = True
                rlt.extend(amount[i] * [i])
                count += amount[i]

        temp = rlt[0]
        rlt[0] = rlt[minIdx]
        rlt[minIdx] = temp

        rltStr = map(str, rlt)
        print ''.join(rltStr)
    except:
        break
