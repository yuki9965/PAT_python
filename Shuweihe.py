__author__ = 'Yaicky'
import sys
array = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


# for line in sys.stdin:
line = raw_input()
result1,result2 = [],[]
sum = 0
s= line.split()
# print(s)
num = int(s[0])
rate = int(s[1])

while num:
    result1.append(array[num%rate])
    num /= rate

for n in result1[::-1]:
    sum += array.index(n)

while sum:
    result2.append(array[sum%rate])
    sum /= rate

result2 = result2[::-1]
print(''.join(result2))