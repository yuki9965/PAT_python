__author__ = 'Yaicky'
import sys
s1,s2 = map(str, raw_input().strip().split())
flag = 0
list = list(s2)
print sys.version
for a in list:
    try:
        pos = s1.index(a)

        if pos == 0:
            s1 = s1[1:]

        else:
            s1 = s1[0:pos]+s1[pos+1:]
    except ValueError:
        flag = 1
        print("No")
        break
if flag == 0:
    print "Yes"

# import copy
# try:
#     while 1:
#         s1,s2 = map(str, raw_input().strip().split())
#         list = list(s2)
#         temp = copy.deepcopy(list)
#         flag = 0
#         for a in temp:
#             try:
#                 pos = s1.index(a)
#                 if pos == 0:
#                     s1 = s1[1:]
#                 else:
#                     s1 = s1[0:pos]+s1[pos+1:]
#                 list.remove(a)
#             except ValueError:
#                 flag = 1
#                 print 'No'
#                 break
#         if flag == 0:
#             print 'Yes'
# except EOFError:
#     pass