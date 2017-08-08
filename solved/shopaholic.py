#!/bin/env python

for _ in range(int(input())):
    input()
    prices = sorted(map(int, input().split()), reverse=True)
    #print(prices)
    print(sum(prices[2::3]))
     
