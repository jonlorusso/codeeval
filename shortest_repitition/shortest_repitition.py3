#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip()
    tl = len(test)
    pstring = ''
    for c in test:
        pstring += c
        p = len(pstring)
        if tl % p == 0 and test == (pstring * int(tl/p)):
            print(p)
            break


test_cases.close()
