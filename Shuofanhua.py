__author__ = 'Yaicky'
str1 = raw_input()
str2 = []
str2 = str1.split(' ')

for i in range(len(str2)-1,-1,-1):
    print str2[i],
    # if i>0:
    #     print ' ',
