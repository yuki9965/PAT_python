__author__ = 'Yaicky'
import copy
while True:
    try:
        n = input()
        numList = map(int, raw_input().strip().split())
        numList.sort()
        rlt = copy.deepcopy(numList)

        last = 9999999
        for i in numList:
            if i == last:
                rlt.remove(i)
            else:
                last = i
        rlt = map(str, rlt)
        print ' '.join(rlt)
    except:
        break