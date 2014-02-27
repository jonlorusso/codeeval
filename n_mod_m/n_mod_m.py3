#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test:
        continue
    n, m = map(int, test.strip().split(','))
    while n > m:
        n -= m
    print(n)

test_cases.close()
