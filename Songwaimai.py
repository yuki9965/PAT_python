__author__ = 'Yaicky'

import sys

for line in sys.stdin:
    m, n = map(int, line.strip().split())
    sum = 0
    if m%2==0 or n%2==0:
        print str(m*n)+'.00'
    else:
        print str(m*n)+'.41'