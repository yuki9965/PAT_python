__author__ = 'Yaicky'
import sys
for line in sys.stdin:
    num = int(line)
    if num == 0:
        num = 0
    else:
        i = 1
        sum = 1
        while i<num:
            sum = (sum+1)*2
            i += 1

        print sum
