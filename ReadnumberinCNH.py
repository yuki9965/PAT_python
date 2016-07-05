__author__ = 'Yaicky'

array = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
rate = ['oh~', 'yeah~', 'Shi', 'Bai', 'Qian', 'Wan', 'Shi', 'Bai', 'Qian', 'Yi']
while True:
    try:
        n = raw_input()
        if int(n) == 0:
            print array[0]
            break
        n = list(n)
        rlt = []
        if '-' in n:
            rlt.append("Fu")
            n.remove('-')


        first = 0

        length = len(n)
        count = 0;

        while (n[len(n)-1] == '0'):
            n.pop()
            first += 1

        lastStr = ''
        for i in range(0,(length-first)):

            if count == 0:
                rlt.append(array[int(n[i])])
                if  lastStr == 'ling' and lastStr == array[int(n[i])]:
                    count += 1
                elif (array[int(n[i])] != 'ling'):
                    if i+1 != length:
                        if length-i == 5 and count == 1:
                            rlt.pop()
                        rlt.append(rate[length-i])
                elif (array[int(n[i])] == 'ling') and length-i == 5:
                    #if lastStr != 'ling':
                    rlt.pop()
                    rlt.append(rate[length-i])


                lastStr = array[int(n[i])]

            else:
                #if length-i != 4:
                rlt.pop()
                if array[int(n[i])] != 'ling':
                    rlt.append(array[int(n[i])])
                    if i+1 != length:
                        rlt.append(rate[length-i])
                #if i+1 != length:
                #     rlt.append(rate[length-i])

                lastStr = array[int(n[i])]
                count = 0


        print ' '.join(rlt)
    except:
        break