#!/usr/bin/env python

import sys

lines = open(sys.argv[1], 'r')
print(sum(map(int, lines)))
lines.close()
