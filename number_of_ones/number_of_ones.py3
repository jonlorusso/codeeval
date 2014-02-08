#!/usr/bin/env python

import sys

for line in open(sys.argv[1], 'r'):
    x = int(line)
    xs = [(x & (2**i)) >> i for i in range(16)]
    print(sum(xs))
