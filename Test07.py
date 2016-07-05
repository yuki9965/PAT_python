# -*- coding: UTF-8 -*-
# -*- coding:utf-8 -*-

def getDis(A, n):
    # write code here
    rlt = 0
    for i in range(n):
        tmp = A[i:]
        if max(tmp) - tmp[0] > rlt:
            rlt = max(tmp) - tmp[0]
    return rlt

print getDis([5386,5384,11054,6345,5816,11757],6)