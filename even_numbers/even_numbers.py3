#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print((int(test) % 2) ^ 1)

test_cases.close()
