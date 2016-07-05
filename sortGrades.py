__author__ = 'Yaicky'

while True:
    try:
        n = input()
        highmarks = []
        lowmarks = []
        highmark = -1
        lowmark = 101
        for i in range(n):
            string = raw_input().strip().split()
            if int(string[2]) < lowmark:
                lowmarks.append([string[0], string[1]])
                lowmark = int(string[2])
            if int(string[2]) > highmark:
                highmarks.append([string[0], string[1]])
                highmark = int(string[2])


        rltStr = highmarks.pop()
        print ' '.join(rltStr)
        rltStr = lowmarks.pop()
        print ' '.join(rltStr)

    except:
        break