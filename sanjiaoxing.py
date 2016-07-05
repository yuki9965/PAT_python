#-*- coding=utf-8 -*-
__author__ = 'Yaicky'

sides = map(int, raw_input().strip().split())
sides.sort()

longside = (sides[2])**2
shortsides = (sides[0])**2 + (sides[1])**2

if longside > shortsides:
    print (u"钝角三角形")
elif shortsides > longside:
    print (u"锐角三角形")
else:
    print(u"直角三角形")