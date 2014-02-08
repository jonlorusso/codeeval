#!/usr/bin/env python

import sys

def detect_cycle(xs):
    ps = []

    for x in xs:
        for p in ps:
            p.append(x)
        ps.append([x])

    print(ps)

for line in open(sys.argv[1], 'r'):
    detect_cycle(map(int, line.split()))
