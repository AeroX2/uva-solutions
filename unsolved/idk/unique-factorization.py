#!/bin/env python
import math

cache = {1: []}
def generate_factors(n):
    if n in cache:
        return cache[n]

    factors = []
    for i in range(math.floor(math.sqrt(n)),1,-1):
        div,mod = divmod(n,i)

        if (mod == 0):
            factors.append((i,div))

    cache[n] = factors[:]
    return factors

n = int(input())
while (n > 0):
    factors = generate_factors(n)
    final_factors = factors[:]

    print("Initial factors", factors)

    #TODO There is duplicates in factors
    while (len(factors) > 0):
        factor = factors.pop()
        sub_factors = []
        for i,number in enumerate(factor):
            test = factor[:i]+factor[i+1:]
            for q in generate_factors(number):
                sub_factors.append(q+test)
        for factor in sub_factors:
            final_factors.append(factor)
            factors.append(factor)

    print(len(final_factors))
    for factor in sorted(final_factors):
        print(' '.join([str(x) for x in factor]))

    n = int(input())
