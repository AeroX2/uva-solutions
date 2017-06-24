#!/bin/env python

n = list(map(int, input().split()))
while (sum(n) != 0):
    print(sum(True for i in range(n[4]+1) if (n[0]*i*i + n[1]*i + n[2])%n[3]==0))
    n = list(map(int, input().split()))

