#!/bin/env python
import sys

string = sys.stdin.read().strip()
for line in string.split('\n'):
    #Change input
    ciggs,k = list(map(int, line.split()))

    butts = 0
    total = ciggs
    while (ciggs > 0):
        ciggs,butts = divmod(ciggs+butts, k)
        total += ciggs
    print(total)
