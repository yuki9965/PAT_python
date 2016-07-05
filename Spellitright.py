__author__ = 'Yaicky'

array = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
while True:
    try:
        strNum = raw_input().strip()
        num = 0
        for i in strNum:
            num += int(i)

        rlt = []
        while num:
            rlt.append(array[num%10])
            num /= 10
        rlt = rlt[::-1]
        print ' '.join(rlt)
    except:
        break