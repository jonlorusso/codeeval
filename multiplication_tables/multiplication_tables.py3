#!/usr/bin/env python

import sys

for i in range(1, 13):
    line = ''
    for j in range(1, 13):
        line += ('%d' % (i * j)).rjust(4)
    print(line.lstrip())
