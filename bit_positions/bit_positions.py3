#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    n, p1, p2 = map(int, test.split(','))

    x = ( n & 2**(p1-1) ) >> (p1 - 1)
    y = ( n & 2**(p2-1) ) >> (p2 - 1)

    print(str(x == y).lower())

test_cases.close()
