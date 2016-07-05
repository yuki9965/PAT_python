__author__ = 'Yaicky'
while True:
    try:
        n = input()
        man = []
        minGrade = 110
        maxGrade = -1
        female = []
        for i in range(n):
            string = raw_input().strip().split()
            if string[1] == 'M':
                if int(string[3]) < minGrade:
                    man.append([string[0],string[2]])
                    minGrade = int(string[3])
            elif string[1] == 'F':
                if int(string[3]) > maxGrade:
                    female.append([string[0],string[2]])
                    maxGrade = int(string[3])
        flag = True
        if maxGrade == -1:
            print "Absent"
            flag = False
        else:
            rltStr = female.pop()
            print ' '.join(rltStr)
        if minGrade == 110:
            print "Absent"
            flag = False
        else:
            rltStr = man.pop()
            print ' '.join(rltStr)
        print maxGrade - minGrade if flag else "NA"

    except:
        break

