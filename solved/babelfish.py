#!/bin/env python

import sys

def next_line():
    for line in sys.stdin.read().strip().split('\n'):
        yield line
    yield ""

dictionary = {}
iterator = next_line()
line = next(iterator)
while (line):
    split = line.split()
    dictionary[split[1]] = split[0]
    line = next(iterator)

line = next(iterator)
while (line):
    if line in dictionary:
        print(dictionary[line])
    else:
        print('eh')
    line = next(iterator)

