__author__ = 'Yaicky'

def nextNum(n):
    if n%2:
        return (3*n+1)/2
    else:
        return n/2

n = input()
data = raw_input().split()
data = map(int, data)

result = data[:]

for i in data[:]:
    while i != 1:
        i = nextNum(i)
        if i in result:
            result.remove(i)

result.sort(reverse=True)
result = map(str, result)
print(' '.join(result))




