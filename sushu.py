__author__ = 'Yaicky'
import math
def isPrime(n):
    flag = False
    if n <= 1:
        return "no"
    elif n == 2:
        return "yes"
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i == 0:
                flag = True
                break
    return "no" if flag else "yes"

while True:
    try:
        n = input()

        print isPrime(n)
    except:
        break