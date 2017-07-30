#!/bin/env python

for _ in range(int(input())):
    n,m = map(int, input().split())
    print((2*n*m - n*n + n)//2 - n)
    #print(sum([m-i for i in range(n)]))
