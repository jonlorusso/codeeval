#!/usr/bin/env python

import sys
import operator

from math import floor
from collections import defaultdict

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    d = defaultdict(int)
    xs  = test.split(',')
    for x in xs:
        d[x] += 1
    sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
    x, c = sorted_d[0]
    if c >= floor(len(xs) / 2):
        print(x)
    else:
        print('None')

test_cases.close()
