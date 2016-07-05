__author__ = 'Yaicky'

def swapMaxAndMin(numList):
    try:
        minNum = min(numList)
        minIdx = numList.index(minNum)
        maxNum = max(numList)
        maxIdx = numList.index(maxNum)

        numList[maxIdx] = minNum
        numList[minIdx] = maxNum

        return numList
    except:
        return numList

while True:
    try:
        n = input()
        numList = map(int, raw_input().strip().split())
        rlt = map(str, swapMaxAndMin(numList))
        print(' '.join(rlt))
    except:
        break