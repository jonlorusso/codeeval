#!/usr/bin/env python

import sys

morse = {}
morse['.-'] = 'A'
morse['-...'] = 'B'
morse['-.-.'] = 'C'
morse['-..'] = 'D'
morse['.'] = 'E'
morse['..-.'] = 'F'
morse['--.'] = 'G'
morse['....'] = 'H'
morse['..'] = 'I'
morse['.---'] = 'J'
morse['-.-'] = 'K'
morse['.-..'] = 'L'
morse['--'] = 'M'
morse['-.'] = 'N'
morse['---'] = 'O'
morse['.--.'] = 'P'
morse['--.-'] = 'Q'
morse['.-.'] = 'R'
morse['...'] = 'S'
morse['-'] = 'T'
morse['..-'] = 'U'
morse['...-'] = 'V'
morse['.--'] = 'W'
morse['-..-'] = 'X'
morse['-.--'] = 'Y'
morse['--..'] = 'Z'
morse['.----'] = '1'
morse['..---'] = '2'
morse['...--'] = '3'
morse['....-'] = '4'
morse['.....'] = '5'
morse['-....'] = '6'
morse['--...'] = '7'
morse['---..'] = '8'
morse['----.'] = '9'
morse['-----'] = '0'

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    words = test.split('  ')
    for word in words:
        print(''.join([morse[c] for c in word.split()]), end="")
        print(' ', end="")
    print()

test_cases.close()
