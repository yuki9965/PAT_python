__author__ = 'Yaicky'
import sys
for line in sys.stdin:
    dividend, divisor, precision = map(int, raw_input().strip().split())

    sys.stdout.write( '0.' )
    for i in xrange(precision):
        dividend *= 10
        sys.stdout.write( str( dividend/divisor ))
        dividend %= divisor
    print