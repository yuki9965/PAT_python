__author__ = 'Yaicky'


class Rat:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
    def __cmp__(self, other):
        return -cmp(self.weight, other.weight)


while True:
    try:
        n = input()
        rats = []
        for i in range(n):
            weight, color = raw_input().strip().split()
            rats.append(Rat(int(weight),color))

        rats.sort()
        for c in rats:
            print c.color
    except:

        break