#!/bin/env python

def bits(n):
    while n:
        yield n&1
        n >>= 1

n = int(input())
while (n > 0): 
    mask = 0
    ones = 0
    for i,bit in enumerate(bits(n)):
        if (bit == 1):
            ones += 1
        
            if (ones % 2 != 0):
                mask |= 1 << i

    print(mask, n & ~mask)

    n = int(input())

