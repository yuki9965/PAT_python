__author__ = 'Yaicky'

str1 = raw_input().upper()
str2 = raw_input().upper()
rlt = []
for i in range(len(str1)):
    if str1[i] not in str2:
        if str1[i] not in rlt:
            rlt.append(str1[i])



print ''.join(rlt)