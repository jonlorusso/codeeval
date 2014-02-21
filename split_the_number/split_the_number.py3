#!/usr/bin/env python

import sys
import re

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    num, pattern = test.split()

    m = re.search('\+', pattern)
    if not m:
        m = re.search('-', pattern)

    left = num[0:m.start()]
    right = num[m.start():]

    print(eval(' '.join([left, m.group(0), right])))

test_cases.close()
