#!/bin/env python
import sys

cache = {1: 1}
def generate(n):
    if (n in cache):
        return cache[n] 

    if (n % 2 != 0):
        cache[n] = 1+generate(3*n+1)
    else:
        cache[n] = 1+generate(n/2)
    return cache[n]

outputs = []
lines = sys.stdin.read().strip()
for line in lines.split('\n'):
    input_numbers = list(map(int, line.split()))
    numbers = sorted(input_numbers)

    max_length = 0
    for number in range(numbers[0], numbers[1]+1):
        max_length = max(max_length,generate(number))
    print(input_numbers[0], input_numbers[1], max_length)

    
