#!/usr/bin/env python

from itertools import islice
import math

def palindrome(x):
    length = len(x)
    l1 = x[0:int(length/2)]
    l2 = x[math.ceil(length/2):]
    return list(l1) == list(reversed(l2))

def prime(x):
    r = range(2, int(math.sqrt(x)) + 1)
    return not(any([x % i == 0 for i in r]))

def primes():
    i = 2
    while True:
        if prime(i):
            yield str(i)
        i += 1

print(max(filter(palindrome, list(islice(primes(), 1000)))))
