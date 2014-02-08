#!/usr/bin/env python

import sys

def multiples(n):
    i = 1
    while True:
        yield n * i
        i += 1

for line in open(sys.argv[1], 'r'):
    x, n = line.split(',')
    print(next(m for m in multiples(int(n)) if m > int(x)))
