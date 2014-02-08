#!/usr/bin/env python

from itertools import islice
import math

def prime(x):
    r = range(2, int(math.sqrt(x)) + 1)
    return not(any([x % i == 0 for i in r]))

def primes():
    i = 2
    while True:
        if prime(i):
            yield i
        i += 1

print(sum(list(islice(primes(), 1000))))
