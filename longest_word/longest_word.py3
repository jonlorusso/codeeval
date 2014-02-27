#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    longest_word = ''

    words = test.strip().split()
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(longest_word)

test_cases.close()
