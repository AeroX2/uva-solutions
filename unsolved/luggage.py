#!/bin/env python

for _ in range(int(input())):
    suitcases = sorted(map(int, input().split()))

    div,mod = divmod(sum(suitcases), 2)
    if (mod != 0):
        print("NO")
        continue

    #Find an arrangement of suitcases that sums up
    #to div


