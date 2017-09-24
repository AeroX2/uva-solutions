#!/bin/env python

from heapq import heappush,heappop

n = int(input())
while (n):
    numbers = [int(x) for x in input().split()]

    queue = []
    for n in numbers:
        heappush(queue,n);

    total = 0
    while (len(queue) > 1):
        n1 = heappop(queue)
        n2 = heappop(queue)
        t = n1 + n2
        total += t
        heappush(queue, t)
    print(total)
    
    n = int(input())

