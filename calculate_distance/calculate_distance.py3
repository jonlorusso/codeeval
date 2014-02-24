#!/usr/bin/env python

import sys
import re

from math import sqrt

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    x1, y1, x2, y2 = map(int, re.findall('-?\d+', test.strip()))
    print(int(sqrt(abs(x1-x2)**2 + abs(y1-y2)**2)))

test_cases.close()
