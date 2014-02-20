#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

def sum_of_squares(x):
    return sum([int(i)**2 for i in x])

def happy(x):
    chain = []
    sq = sum_of_squares(x)

    while True:
        if sq == 1:
            return True
        if sq in chain:
            return False
        chain.append(sq)
        sq = sum_of_squares(str(sq))

for test in test_cases:
    if happy(test.strip()):
        print(1)
    else:
        print(0)
    
test_cases.close()
