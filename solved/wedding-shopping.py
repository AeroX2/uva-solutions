#!/bin/env python

from copy import deepcopy

cache = {}
def helper(depth,count,garments,money):
    if (depth >= len(garments)):
        return count
    if ((depth,count) in cache):
        return cache[(depth,count)]

    maximize = 0
    for garment in garments[depth]:
        if (count+garment <= money):
            output = helper(depth+1, count+garment, garments, money)
            maximize = max(maximize, output)

    cache[(depth,count)] = maximize

    return maximize

for i in range(int(input())):
    m,shops = map(int,input().split())

    garments = []
    for garment in range(shops):
        shop = map(int, input().split()[1:])
        garments.append(list(shop))
    garments.reverse()

    cache = {}
    answer = helper(0,0,garments,m)
    if (answer == 0):
        print("no solution")
    else:
        print(answer)


