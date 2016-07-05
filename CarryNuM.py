__author__ = 'Yaicky'
def calCarry(num1, num2, carry):
    carry = (num1 + num2 + carry) / 10
    return carry
while True:
    a, b = map(int, raw_input().strip().split())
    if a==0 and b==0:
        break
    carry = count = 0

    while a%10 or b%10 or a or b:
        carry = calCarry(a%10, b%10, carry)
        if carry:
            count += 1
        a /= 10
        b /= 10

    if count == 0:
        print 'NO carry operation.'
    elif count == 1:
        print '1 carry operation.'
    else:
        print '%d carry operations.' % (count)
