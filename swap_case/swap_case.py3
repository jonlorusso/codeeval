#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    print(test.swapcase().strip())

test_cases.close()
