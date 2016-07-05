__author__ = 'Yaicky'

import sys

def findcoin(n):
    if n == 1:
        return 0
    elif n <= 3:
        return 1
    else:
        metage, rest, count = 0, 0, 0
        metage = (n+2)/3
        rest = n - metage*2
        count = 1+ findcoin(max(metage,rest))
        return count

for line in sys.stdin:
    n = int(line)
    if n == 0:
        break
    print(findcoin(n))
