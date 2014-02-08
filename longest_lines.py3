#!/usr/bin/env python

import sys
from operator import itemgetter 

count = None

class Tree:
    def __init__(self, line):
        self.left = None
        self.right = None
        self.line = ( line, len(line) )

    def add(self, line):
        length = len(line)
        if length > self.line[1]:
            if self.right: self.right.add(line)
            else: self.right = Tree(line)
        else:
            if self.left: self.left.add(line)
            else: self.left = Tree(line)
    
    def print_top(self, n):
        if self.right: n = self.right.print_top(n)

        if n > 0:
            print(self.line[0])
            n -= 1

            if n > 0 and self.left:
                n = self.left.print_top(n)

        return n

tree = None

for line in open(sys.argv[1], 'r'):
    if not count:
        count = int(line)
        continue

    line = line.rstrip()
    if not tree:
        tree = Tree(line)
    else:
        tree.add(line)

tree.print_top(count)
