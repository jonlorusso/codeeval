#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

def numeral(char, value, total):
    count = total / value
    print(char * int( count ), end = '')
    return total - ( int(count) * value )

for test in test_cases:
    x = int(test)

    x = numeral('M', 1000, x)
    x = numeral('D', 500, x)
    x = numeral('C', 100, x)
    x = numeral('XC', 90, x)
    x = numeral('L', 50, x)
    x = numeral('XL', 40, x)
    x = numeral('X', 10, x)
    x = numeral('IX', 9, x)
    x = numeral('V', 5, x)
    x = numeral('IV', 4, x)
    x = numeral('I', 1, x)
    print()

test_cases.close()
