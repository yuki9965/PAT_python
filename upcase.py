__author__ = 'Yaicky'
import math
import re
while True:
    try:
        # string = map(str, raw_input().strip().split('_'))
        # rlt = string[0:1]
        # for i in string[1:]:
        #     rlt.append(i.title())
        #
        # print ''.join(rlt)
        # aa = "Hello  world."
        # #print aa.replace(" ", "%20",len(aa))
        # print abs(-1)
        # kll = [1,2,3,4]
        # asda = 'sd adqwe'
        # print kll[::-1]
        # print asda[::-1]
        # string = raw_input().strip()
        # print string
        # s = string[::-1]
        # print ''.join(reversed(string))
        # length = input()
        # numbers = map(int, raw_input().strip().split())
        # numbers.sort()
        # print numbers[length-1], numbers[0]
        string = raw_input()
        origin = raw_input()
        target = raw_input()
        partten = re.compile((r'\b'+origin+r'\b'))
        print re.sub(partten, target, string)
    except:
        break


