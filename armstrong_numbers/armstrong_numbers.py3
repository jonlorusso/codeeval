#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    print(sum([int(c)**len(test) for c in test]) == int(test))

test_cases.close()
