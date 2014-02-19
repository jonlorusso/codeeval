#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')

fibs = {}

def fib(n):
    global fibs

    res = fibs.get(n, None)
    if res:
        return res

    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)

    fibs[n] = res
    return res

for test in test_cases:
    print(fib(int(test)))

test_cases.close()
