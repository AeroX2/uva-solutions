#!/bin/env python

#https://stackoverflow.com/questions/19345627/python-prime-numbers-sieve-of-eratosthenes 
#This version seems to be faster than anything I have tested
def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1))

    s[1] = 0
    
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn+1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

primes = list(sieve(10**7))

n = abs(int(input()))
while (n != 0):

    i = 0
    count = 0
    max_p = 0
    while (n > 1):
        p = primes[i]

        if (p*p > n):
            break

        if (n%p == 0):
            count += 1
            max_p = p

        while (n%p == 0):
            n //= p

        i += 1

    if (n > 1):
        count += 1
        max_p = n

    print(max_p if count > 1 else -1)

    n = abs(int(input()))

