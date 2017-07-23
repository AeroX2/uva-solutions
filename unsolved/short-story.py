#!/bin/env python

import sys

def lines():
    for line in sys.stdin.read().split('\n'):
        yield line.strip()
    yield ''

iterator = lines()
line = next(iterator)
while (line):
    _,l,c = map(int, line.split())
    line = next(iterator)

    current_char = 0
    current_line = 0
    current_page = 1

    for word in line.split():
        current_char += len(word)

        if (current_char >= c):
            current_char -= c
            current_line += 1

        if (current_line >= l):
            current_line = 0
            current_page += 1

        #print(word, current_char, current_line)
        current_char += 1

    print(current_page)

    line = next(iterator)


