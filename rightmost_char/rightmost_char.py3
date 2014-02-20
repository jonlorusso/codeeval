#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test:
        next
    text, char = test.strip().split(',')
    found = False
    for i in range(len(text) - 1, 0, -1):
        if text[i] is char:
            print(i)
            found = True
            break
    if not found:
        print(-1)


test_cases.close()
