__author__ = 'Yaicky'

while True:
    try:
        row = input()
        pos = [0] * row
        speed = [0] * row
        posA = 0
        for i in range(row):
            pos[i], speed[i]= map(int, raw_input().strip().split())
            if speed[i] == 0:
                posA = pos[i]

        leftGoR, rightGoL = [], []

        for i in range(row):
            if pos[i] < posA and speed[i] > 0:
                leftGoR.append(100-pos[i])
            elif pos[i] > posA and speed[i] < 0:
                rightGoL.append(pos[i])
        #print(pos, speed)

        leftNum = len(leftGoR)
        rightNum = len(rightGoL)
        if leftNum == rightNum:
            print "Cannot fall!"
        elif leftNum > rightNum:
            leftGoR.sort(reverse=True)
            print leftGoR[leftNum-rightNum-1]
        else:
            rightGoL.sort(reverse=True)
            print rightGoL[rightNum-leftNum-1]
    except:
        break