#coding=utf-8

__author__ = 'Yaicky'

M,N=map(int,raw_input().split(" "))
Max=10000000
def find(M,N):
    ans=[0,2]
    for i in xrange(3,Max):
        if len(ans)>N:
            break
        j=1
        flag=1
        while ans[j]<=i**0.5:
            if i%ans[j]==0:   #能被整除  立马退出不用看其他的
                flag=0
                break
            j+=1
        if flag:
            ans.append(i)
    return ans
ans=find(M,N)
i=M
count=1
while i<=N:
    if count%10==0:
        print ans[i]
    else:
        print ans[i],
    count+=1
    i+=1