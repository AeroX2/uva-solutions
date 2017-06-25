#!/bin/env python

import sys

def expand(l):
    for i in l[:]:
        for ii in range(2,i):
            l.append(ii)
    return l

def product(l):
    p = 1
    for i in l:
        p *= i
    return p

def consume():
    string = sys.stdin.read().strip().replace('\n',' ')
    for number in string.split():
        yield int(number)

iterator = consume()
number = (next(iterator), next(iterator))
while (number[0] != 0 or number[1] != 0):
    factorials_1 = [next(iterator) for _ in range(number[0])]
    factorials_2 = [next(iterator) for _ in range(number[1])]

    factorials_1 = filter(lambda x: x > 1, factorials_1)
    factorials_2 = filter(lambda x: x > 1, factorials_2)

    #I thought this code would be notoriuosly slow but hey it works TM
    factorials_1 = expand(list(factorials_1))
    factorials_2 = expand(list(factorials_2))

    if (product(factorials_1) == product(factorials_2)):
        print("YES")
    else:
        print("NO")

    number = (next(iterator), next(iterator))

