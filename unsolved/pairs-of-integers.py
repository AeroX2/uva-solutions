#!/bin/env python

from math import log,floor

def get_pairs(x):
    for i in range(floor(log(x,1)-1),x+1):
        if str(i) in str(x - i)a
            yield (i, x-i)

for _ in range(int(input())):
    #Read blank
    input()
    n = int(input())
    pairs = get_pairs(n)


