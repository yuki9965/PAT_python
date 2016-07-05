__author__ = 'Yaicky'

def calFactors(n):
    factors = [0]
    if n == 1:
        return factors
    for i in range(1,n):
        if n%i == 0:
            factors.append(i)
    return factors

def isPerfectNum(n, factors):
    num = sum(factors)
    if n == num:
        return True
    else:
        return False

while True:
    try:
        n = input()
        rlt = []
        for i in range(1,n+1):
            factors = calFactors(i)
            if isPerfectNum(i, factors):
                rlt.append(str(i))

        print ' '.join(rlt)
    except:
        break
