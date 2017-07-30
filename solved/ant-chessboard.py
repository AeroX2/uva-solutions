#!/bin/env python

n = int(input())
while (n > 0):
    i = 1
    a = 1
    while (n > a):
        n -= a
        a += 2
        i += 1

    mid = (a // 2)+1
    if (n > mid):
        d = 2*mid - n
        print('%d %d' % ((i,d) if i%2==0 else (d,i)))
    else:
        print('%d %d' % ((n,i) if i%2==0 else (i,n)))

    n = int(input())

