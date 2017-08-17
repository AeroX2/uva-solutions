#!/bin/env python

def subset_sum(remaining, value, partial=[]):
    summed = sum(partial)
    if (summed == value):
        return partial

    if (summed > value):
        return None

    for i,num in enumerate(remaining):
        result = subset_sum(remaining[i+1:], value, partial+[num])
        if (result is not None):
            return result
    return None

for _ in range(int(input())):
    suitcases = sorted(map(int, input().split()))

    div,mod = divmod(sum(suitcases), 2)
    if (mod != 0):
        print("NO")
        continue

    result1 = subset_sum(suitcases, div) 
    if (result1 is None):
        print("NO")
        continue

    for num in result1:
        suitcases.remove(num)
        
    result2 = subset_sum(suitcases, div) 

    if (result1 is not None and
        result2 is not None):
        print("YES")
    else:
        print("NO")
        

