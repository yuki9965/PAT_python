__author__ = 'Yaicky'

while True:
    try:
        numList = map(int, raw_input().strip().split())
        count = [0]*11
        if len(numList):
            for i in numList:
                count[i] += 1

            maxNum = max(count)
            print(count.index(maxNum))
    except:
        break
