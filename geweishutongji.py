__author__ = 'Yaicky'

while True:
    try:
        strList = raw_input().strip()
        strList = list(strList)
        strList = map(int, strList)
        # print strList
        rlt = [0]*10

        for i in strList:
            rlt[i] += 1

        for i in range(10):
            if rlt[i] == 0:
                continue
            print "%d:%d" %(i, rlt[i])
    except:
        break