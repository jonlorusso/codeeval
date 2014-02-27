#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    writer, key = test.split('|')

    for num in key.split():
        print(writer[int(num) -1], end='')

    print()

test_cases.close()
