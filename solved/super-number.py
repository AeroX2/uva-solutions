#!/bin/env python

def helper(i, m, final):
    mod = final % i
    first = i-mod if mod != 0 else 0

    for num in range(first, 10, i):
        new_num = final+num
        if (i == m):
            return new_num

        output = helper(i+1, m, new_num*10)
        if (output != -1):
            return output
    return -1

for i in range(int(input())):
    n,m = map(int, input().split())

    start = pow(10,n-1) + ((n - pow(10,n-1)) % n)
    while (start < pow(10,n)):
        output = helper(n+1, m, start*10)
        if (output != -1):
            break
        start += n

    print('Case %d: %d' % (i+1,output))

