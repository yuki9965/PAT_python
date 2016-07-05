__author__ = 'Yaicky'

array = [1]
a,b = 1,2
for i in range(1,100001):
    a,b = b,a+b
    array.append(a%1000000)

while True:
    s = raw_input()
    if s=='':
        break
    else:
        num = int(s)

    print(array[num-1])

