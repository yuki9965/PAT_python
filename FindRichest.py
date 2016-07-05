__author__ = 'Yaicky'
while True:
    try:
        m, n = map(int, raw_input().strip().split())
        if m or n:
            richList = map(int, raw_input().strip().split())
            richList.sort()

            while n and len(richList)!=0:
                print richList.pop(),
                n -= 1
        elif m==0 and n==0:
            break
        print

    except:
        break