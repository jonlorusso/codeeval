#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    words = test.split()
    print(' '.join(map(lambda w: w[0].capitalize() + w[1:], words)))

test_cases.close()
