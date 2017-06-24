#!/bin/env python

import sys

lines = []
string = sys.stdin.read()
for line in string.split('\n'):
    lines.append(' '.join(w[::-1] for w in line.split()))

for line in lines:
    if (line):
        print(line)
