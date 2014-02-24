#!/usr/bin/env python

import sys

digits = {}
digits['zero'] = 0
digits['one'] = 1
digits['two'] = 2
digits['three'] = 3
digits['four'] = 4
digits['five'] = 5
digits['six'] = 6
digits['seven'] = 7
digits['eight'] = 8
digits['nine'] = 9

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    xs = [digits[d] for d in test.strip().split(';')]
    print(''.join(map(str, xs)))

test_cases.close()
