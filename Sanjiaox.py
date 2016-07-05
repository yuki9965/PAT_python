__author__ = 'Yaicky'
import sys
for line in sys.stdin:

    s = line.split()
    a = int(s[0])
    b = int(s[1])
    c = int(s[2])


    if (a+b>c) and (b+c>a) and (a+c>b):
        print("Yes")
    else:
        print("No")