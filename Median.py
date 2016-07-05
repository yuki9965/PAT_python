__author__ = 'Yaicky'

while True:
    try:
        numList1 = map(int, raw_input().strip().split())
        numList1.remove(numList1[0])
        numList2 = map(int, raw_input().strip().split())
        numList2.remove(numList2[0])

        numList1.extend(numList2)
        numList1.sort()

        if len(numList1)%2:
            pos = len(numList1) / 2
        else:
            pos = len(numList1) / 2 - 1
        print numList1[pos]
    except:
        break