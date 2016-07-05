__author__ = 'Yaicky'

def binarySearch(n, rlt):
    left, right = 0, len(rlt)-1
    mid = (left + right) / 2

    while left != right:
        if rlt[mid] == n:
            return mid, rlt[mid]
        elif rlt[mid] > n:
            if rlt[mid-1] <= n:
                return mid-1, rlt[mid-1]
            else:
                right = mid-1
        elif rlt[mid] < n:
            if rlt[mid+1] >= n:
                return mid, rlt[mid]
            else:
                left = mid+1

        mid = (left + right) / 2

rlt = [0, 1]
for i in range(2, 25):
    rlt.append(rlt[i-1]+(4*i-2))

while True:
    try:
        string = raw_input().strip().split(' ')
        num = int(string[0])
        ch = string[1]

        if num == 1:
            print ch
            print 0
        else:
            line, rest = binarySearch(num, rlt)
            rest = num -rest

            for i in range(line,0,-1):
                str = ' '*(line-i) + ch*(2*i-1)
                print str
            for i in range(2, line+1):
                str = ' '*(line-i) + ch*(2*i-1)
                print str
            print rest
            # print rlt
            # print binarySearch(num, rlt)
    except:
        break
