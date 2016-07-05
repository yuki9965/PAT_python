__author__ = 'Yaicky'
modifyDic = {'1':'@', '0':'%', 'l':'L', 'O':'o'}
modifyNeed = ['1', '0', 'l', 'O']

def needModified(pwd):
    flag = False
    for s in pwd:
        if s in modifyNeed:
            flag = True
            break

    return flag

def modifyPwd(pwd):
    rlt = ''
    for s in pwd:
        if s in modifyNeed:
            rlt += modifyDic[s]
        else:
            rlt += s
    return rlt

while True:
    try:
        n = input()
        count = 0
        rlt = []
        for i in range(n):
            string = raw_input().strip().split()
            if needModified(string[1]):
                string[1] = modifyPwd(string[1])
                count += 1
                rlt.append(string)

        if count == 0:
            if n == 1:
                print "There is 1 account and no account is modified"
            else:
                print "There are %d accounts and no account is modified" % n
        else:
            print count
            for i in rlt:
                print ' '.join(i)

    except:
        break