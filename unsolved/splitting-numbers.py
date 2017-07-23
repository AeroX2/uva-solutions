#!/bin/env python

n = int(input())
while (n > 0): 
    mask = 0x55555555
    print(len(bin(n)))
    a = (1 << len(bin(n))-2) | (n & mask)
    b = (1 << len(bin(n))-2) | (n & ~mask)
    print(a,b)

    n = int(input())

