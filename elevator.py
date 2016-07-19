__author__ = 'Yaicky'

while True:
    try:

        floors = map(int, raw_input().strip().split())
        floors = floors[1:]
        count = up = down = 0
        last = -1
        for i in floors:
            if count == 0:
                up += i
            else:
                if i>last:
                    up += i-last
                else:
                    down += last-i

            count += 1
            last = i
        # down += last
        print up*6+count*5+down*4
    except:
        break
