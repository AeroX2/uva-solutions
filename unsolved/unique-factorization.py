#!/bin/env python
import math

#TODO Misinterpetated the question
#Not the roots but all the factors, so revursive factors of factors

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

#def roots(k):
#    output = []
#
#    i = 2
#    root = k ** (1.0/i)
#    while (root >= 2):
#        if (root.is_integer()):
#            output.append((int(root),i))
#        i+=1
#        root = k ** (1.0/i)
#    return output

n = int(input())
while (n > 0):
    factors = generate_factors(n)

    output = []

    count = len(factors) // 2
    print(factors)
    for i in range(count):
        for root in roots(factors[i]):
            s = ' '.join(map(str, [root[0] for _ in range(root[1])]))
            output.append('%d %s' % (factors[i], s))

        for root in roots(factors[-i-1]):
            s = ' '.join(map(str, [root[0] for _ in range(root[1])]))
            output.append('%d %s' % (factors[-i-1], s))
    
    print(len(output))
    for line in output:
        print(line)
                
    n = int(input())
