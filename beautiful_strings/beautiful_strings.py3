#!/usr/bin/env python

import sys
from collections import defaultdict
import operator

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    d = defaultdict(int)
    for x in test:
        if x.isalpha():
            d[x.lower()] += 1

    sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

    mult = 26
    sum = 0
    for k, v in sorted_d:
        sum = sum + (int(v) * mult)
        mult = mult - 1

    print(sum)


test_cases.close()
