#!/bin/env python
import math

#TODO

cache = {1: 1}
def generate_factors(n):
    if (n in cache):
        return cache[n]

    factors = []
    for i in range(n-1,1,-1):
        if (i in cache):
            factors += cache[i]
        else:
            if (n % i == 0):
                factors.append(i)
                factors += generate_factors(i)
    cache[n] = factors
    return sorted(set(factors))


amount = int(input())
for _ in range(amount):
    n,k = list(map(int, input().split()))
    factors = generate_factors(n)
    print((factors))
    print((cache))
