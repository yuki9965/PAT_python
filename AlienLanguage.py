__author__ = 'Yaicky'
import sys
array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']



# print(s)
num = int(input())
for rate in range(2,17):
    temp = num
    list =[]
    s1=''
    while num:
        list.append(array[num%rate])
        num /= rate
    s1 = ''.join(list)
    if cmp(s1,s1[::-1])==0:
        print rate
        print("Yes")
        break
    if rate == 16:
        print("No")

    num = temp
# for line in sys.stdin:
#     result = []
#     s= line.split()
#     # print(s)
#     num = int(s[0])
#     rate = int(s[1])
#
#     while num:
#         result.append(array[num%rate])
#         num /= rate
#
#     result = result[::-1]
#     print(''.join(result))