#!/bin/env python

for i in range(int(input())):
    n = int(input())
    happy = False

    num = n
    cache = {}
    while True:
        product_sum = 0
        for c in str(num):
            q = int(c)
            product_sum += q*q

        if (num in cache):
            #print(cache)
            if (num == 1):
                happy = True
            break

        cache[num] = product_sum
        num = product_sum
        #print(num)


    print("Case #%d: %d is a%s number." % (i+1,n," Happy" if happy else "n Unhappy"))

