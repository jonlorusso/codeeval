#!/usr/bin/env python

import sys
import operator

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    d = {}

    pos = 1
    for c in test.strip().split():
        if c in d:
            d[c] = 0
        else:
            d[c] = pos
        pos += 1

    sorted_d = sorted(d.items(), key=operator.itemgetter(0))

    found = False
    for k, v in sorted_d:
        if v > 0:
            print(v)
            found = True
            break
    if not found:
        print(0)


test_cases.close()
