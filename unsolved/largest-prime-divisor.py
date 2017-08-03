#!/bin/env python

import math
import time

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
n = int(input())
while (n > 0):
    #Filter out primes larger than sqrt(n)
    for prime in reversed(primes):
        if (prime != n and n % prime == 0):
            print(prime)
            break
    else:
        print(-1)

    n = int(input())

