#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    none = True
    for c in test:
        n = ord(c)
        if 97 <= n <= 106:
            none = False
            print(n - 97, end='')
        if 48 <= n <= 57:
            none = False
            print(c, end='')
    if none:
        print('NONE')
    else:
        print()

test_cases.close()
