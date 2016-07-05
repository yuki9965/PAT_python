__author__ = 'Yaicky'

n = raw_input().split()
num = int(n[0])
shift = int(n[1])%num

s = raw_input().split()
s1 = s[0:num-shift]
s2 = s[num-shift:num]
s2.extend(s1)
print (' '.join(s2))
