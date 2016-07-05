__author__ = 'Yaicky'
while True:
    try:
        line = raw_input().split()
        n = int(line[0])
        alphabet = line[1]
        firstAndLast = [alphabet]*n
        others = [alphabet]+[" "]*(n-2)+[alphabet]

        length = n/2.0
        if (length-n/2) != 0:
            length += 0.5

        for i in range(0,int(length)):
            if i == 0 or i == (length-1):
                print ''.join(firstAndLast)
            else:
                print ''.join(others)
    except:
        break