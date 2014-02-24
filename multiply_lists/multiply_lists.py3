#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    xs1, xs2 = test.split('|')
    pairs = zip(xs1.split(), xs2.split())
    print(' '.join(map(lambda pair: str(int(pair[0]) * int(pair[1])), pairs)))

test_cases.close()
