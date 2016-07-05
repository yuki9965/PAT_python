__author__ = 'Yaicky'


radix = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
weight = [0]*25

def calWeight():
    weight[0] = 1
    for i in range(1, 25):
        weight[i] = radix[i-1] * weight[i-1]



def readNumber(strs):
    nums = map(int, strs.split(','))
    rlt = 0
    for index, num in enumerate(nums):
        rlt += num*weight[len(nums)-1-index]
    return rlt

def creatNumber(ints):
    rltList = []
    i = 0
    while ints!=0:
        rltList.append(str(ints%radix[i]))
        ints /= radix[i]
        i += 1

    rltList = rltList[::-1]
    rltStr = ','.join(rltList)
    return  rltStr

calWeight()

while True:
    try:
        x, y = raw_input().strip().split()
        aft_x = readNumber(x)
        aft_y = readNumber(y)
        #print aft_y,aft_x
        if aft_x+aft_y == 0:
            break
        print creatNumber(aft_y+aft_x)

    except:
        break