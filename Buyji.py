__author__ = 'Yaicky'

while True:
    try:
        money = input()
        for x in range(0,101):
            for y in range(0,101):
                z = 100 - x - y
                if(((5*x + 3*y + z/3.0) <= money)):
                    print "x=%d,y=%d,z=%d"%(x,y,z)
    except:
        break