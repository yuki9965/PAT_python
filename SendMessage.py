__author__ = 'Yaicky'
n = []
i=2
while(i):
    m = input()
    n.append(m)
    i =i-1


for i in n:
    if i == 2:
        print 1
    elif i ==3:
        print 2
    else :
        temp=0
        temp = i-1
        i = i-1
        while(i>=2):
            temp = temp*i
            i = i-1
        print temp