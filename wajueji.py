__author__ = 'Yaicky'

while True:
    try:

        #n = input()
        #numList = map(int, raw_input().strip().split(' '))
        #scores = map(int, raw_input().strip().split(' '))
        allNums = map(int, raw_input().strip().split(' '))
        n = allNums[0]
        numList , scores = [], []
        numList = allNums[1:n+1]
        scores = allNums[n+2:]

        numList.sort()
        #scores = scores[1:]
        rlt = []

        for i in scores:
            try:
                idx = numList.index(i)
                count = 0
                while numList[idx] == i:
                    idx += 1
                    count += 1
                rlt.append(str(count))
            except:
                rlt.append('0')

        print ' '.join(rlt)
    except:
        break