__author__ = 'Yaicky'

while True:
    try:
        num1, num2 = raw_input().strip().split()
        num1, num2 = list(num1), list(num2)

        sumup = 0
        for n1 in num1:
            for n2 in num2:
                sumup += int(n1) * int(n2)

        print sumup
        # print num1
    except:
        break