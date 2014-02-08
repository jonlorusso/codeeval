#!/usr/bin/env python

import sys

def reverse_words(s):
    words = s.split()
    print(' '.join(list(reversed(words))))

for line in open(sys.argv[1], 'r'):
    reverse_words(line)
