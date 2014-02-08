#/usr/bin/env python

import sys

def fizzbuzz(a, b, n):
    for i in range(1, n+1):
        fizz = i % a == 0
        buzz = i % b == 0

        if fizz and buzz:
            print("FB", end="")
        elif fizz:
            print("F", end="")
        elif buzz:
            print("B", end="")
        else:
            print(i, end="")

        if i < n:
            print(" ", end="")

    print()

for line in open(sys.argv[1], 'r'):
    a, b, n = line.split()
    fizzbuzz(int(a), int(b), int(n))
