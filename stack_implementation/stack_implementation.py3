#!/usr/bin/env python

import sys

def process_stack(line):
    stack = [ int(x) for x in line.split() ]

    while stack:
        print(stack.pop(), end="")
        if stack:
            print(' ', end="")
            stack.pop()
    print()

for line in open(sys.argv[1], 'r'):
    process_stack(line.rstrip())
