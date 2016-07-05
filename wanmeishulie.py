__author__ = 'Yaicky'

n,p = map(int, raw_input().strip().split())
array = map(int, raw_input().strip().split())
array.sort(reverse=True)
maxlength = 0
curlength = 0
i = 0
for j in range(n):
    while i<n:
        if array[i]*p<array[j]:
            curlength = i-j
            break
        i += 1

    if curlength > maxlength:
        maxlength = curlength

print maxlength