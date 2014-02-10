#!/usr/bin/env python

import sys
from collections import deque

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    xs, sum = test.rstrip().split(';')
    need = deque()

    sum = int(sum)
    pairs = []
    for x in xs.split(','):
        x = int(x)
        if need:
            for n in need:
                if x is n[0]:
                    pairs.append('%d,%d' % (n[1], x))
                    break

        need.appendleft(((sum - x), x))

    if pairs:
        print(';'.join(sorted(pairs)))
    else:
        print('NULL')

test_cases.close()
