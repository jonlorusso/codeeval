#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

def output(count, curr, first, last):
    if not first:
        print(' ', end="")

    print('%d %s' % (count, curr), end="")
    if last:
        print()

for test in test_cases:
    xs = test.split()
    count = 0
    curr = None
    first = True
    for x in xs:
        if not curr:
            curr = x
            count = 1
        elif x != curr:
            output(count, curr, first, False)
            first = False
            curr = x
            count = 1
        else:
            count += 1
    output(count, curr, first, True)

test_cases.close()
