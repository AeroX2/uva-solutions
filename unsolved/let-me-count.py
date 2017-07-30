#!/bin/env python

import sys

def lines():
    for line in sys.stdin.read().split('\n'):
        yield line.strip()
    yield ''

iterator = lines()
line = next(iterator)
while (line):
    n = int(line)

    cache = []
    stack = [(n,[])]
    while (len(stack) > 0):
        cents,l = stack.pop()
        for coin in [1,5,10,25,50]:
            div,rem = divmod(cents, coin)

            new_l = sorted(l+[coin])
            #if (new_l in cache):
            #    continue

            if (rem == 0):
                print('adding', div,rem)
                cache.append(new_l)
            elif (div > 0 and rem > 0):
                print(coin,rem)
                stack.append((rem,new_l))

    output = len(cache)
    if (output != 1):
        print('There are %d ways to produce %d cents of change.' % (output, n))
    else:
        print('There is only 1 way to produce %d cents of change.' % n)

    line = next(iterator)

