__author__ = 'Yaicky'

while True:
    try:
        n = input()
        numList = map(int, raw_input().strip().split())
        target = input()

        print numList
        try:
            print numList.index(target)
        except:
            print "-1"
    except:
        break