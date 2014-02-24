#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    set1, set2 = map(lambda x: set(x.split(',')), test.strip().split(';'))
    intersection = set()
    for x in set1:
        if x in set2:
            intersection.add(x)
    print(','.join(sorted(list(intersection))))

test_cases.close()
