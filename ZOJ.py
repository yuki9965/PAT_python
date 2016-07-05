__author__ = 'Yaicky'
import sys
while True:
    try:
        s = raw_input()
        if s == 'E':
            break
        znum = onum = jnum = 0
        for i in s:
            if i == 'Z':
                znum += 1
            elif i == 'O':
                onum += 1
            elif i == 'J':
                jnum += 1

        while znum or onum or jnum:
            if znum:
                sys.stdout.write('Z')
                znum -= 1
            if onum:
                sys.stdout.write('O')
                onum -= 1
            if jnum:
                sys.stdout.write('J')
                jnum -= 1
        sys.stdout.write('\n')
    except:
        break