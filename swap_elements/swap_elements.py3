#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    xs, swaps = test.split(' : ')

    xs = xs.split()
    swaps = swaps.split(',')

    for swap in swaps:
        start, end = map(int, swap.split('-'))
        xs[start], xs[end] = xs[end], xs[start]

    print(' '.join(xs))


test_cases.close()
