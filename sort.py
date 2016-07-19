__author__ = 'Yaicky'
while True:
    try:
        n = input()
        nums = []
        nums = map(int, raw_input().strip().split(' '))
        nums.sort()
        for i in nums:
            print i,

    except:
        break