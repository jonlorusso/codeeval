#!/usr/bin/env python

import sys

from collections import defaultdict

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    i = 0
    d = defaultdict(int)
    for c in test.strip():
        d[c] -= 1
        d[str(i)] += int(c)
        i += 1
    if sum(d.values()) == 0:
        print(1)
    else:
        print(0)

test_cases.close()
