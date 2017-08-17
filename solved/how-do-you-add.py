#!/bin/env python
import math

def nCr(n,r):
    f = math.factorial
    return f(n) // (f(r) * f(n-r))

n,k = map(int, input().split())
while (n != 0 and k != 0):
    print(nCr(n+k-1, k-1) % 1000000)
    n,k = map(int, input().split())
