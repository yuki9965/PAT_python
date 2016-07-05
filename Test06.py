# -*- coding: UTF-8 -*-
__author__ = 'Yaicky'
# 题目：斐波那契数列。

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]

    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print fib(10)