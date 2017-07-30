#!/bin/env python
import math

#TODO Time limit exceeded

def generate_factors(n,k):
    if (n in cache):
        return cache[n]

    factors = []
    for i in range(n-1,1,-1):
        if (i in cache):
            factors += cache[i]
        elif (n % i == 0 and n % k != 0):
            factors.append(i)
            factors += generate_factors(i,k)
    cache[n] = factors
    return sorted(set(factors))


amount = int(input())
for _ in range(amount):
    n,k = list(map(int, input().split()))
    cache = {1: 1}
    factors = generate_factors(n,k)
    if (1 % k != 0):
        factors.append(1)
    if (n % k != 0):
        factors.append(n)
    print(sum(factors))
