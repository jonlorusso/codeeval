#!/usr/bin/env python

import sys
from itertools import permutations

#def max_subarray(A):
##    max_ending_here = max_so_far = 0
#    for x in A:
#        max_ending_here = max(0, max_ending_here + x)
#        max_so_far = max(max_so_far, max_ending_here)
#    return max_so_far


def max_sum(xs):
    curr_sum = 0
    max_sum = 0
    for x in xs:
        curr_sum = curr_sum + x if curr_sum + x > 0 else 0
        max_sum = max(max_sum, curr_sum)
    return max_sum

for line in open(sys.argv[1], 'r'):
    print(max_sum(list(map(int, line.split(',')))))

