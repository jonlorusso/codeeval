#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    xs = test.split()
    i = int(xs[-1])
    xs = xs[:-1]

    if len(xs) >= i:
        print(xs[-i])

test_cases.close()
