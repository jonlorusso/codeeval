#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

#
# NOTE: Assumes positive integers.
#

for test in test_cases:
    num = -1
    nums = []
    xs = test.strip().split(',')
    for x in xs:
        if x != num:
            num = x
            nums.append(x)
    print(','.join(nums))

test_cases.close()
