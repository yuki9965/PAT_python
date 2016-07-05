__author__ = 'Yaicky'

numa = ord('A')
def decode(c):
    numc = ord(c) - 5
    rltc = numc if numc >= numa else numc+26
    return chr(rltc)

while True:
    s = raw_input()
    if s == 'ENDOFINPUT':
        break
    elif s=='START' or s=='END':
        continue
    else:
        rlt = ''
        for i in s:
            if 'A' <= i <= 'Z':
                rlt += decode(i)
            else:
                rlt += i
        print(rlt)

