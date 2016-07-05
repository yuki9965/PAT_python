__author__ = 'Yaicky'

array = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']

strs = raw_input()

sumup = map(int,strs)
sumup = str(sum(sumup))
for i in range(len(sumup)):
    print array[int(sumup[i])],