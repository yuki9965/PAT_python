__author__ = 'Yaicky'

def greatestcd(a, b):
    while b:
        a, b = b, a%b
    return a
while True:
    try:
        a, b = map(int, raw_input().strip().split())
        print greatestcd(a, b)
    except:
        break