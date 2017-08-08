#!/bin/env python

from math import log,floor

def get_pairs(x):
    #TODO There is a trick to optimize this loop
    #I think it has something to do with index < previous_index
    for i in range(floor(log(x,10)-1),x+1):
        if i == x-i:
            continue

        if (i in range(11)):
            i_s = "0"+str(i)
        else:
            i_s = str(i)

        x_s = str(x-i)
        #print(i_s,x_s)

        previous_index = 0
        valid = True
        for digit in i_s:
            index = x_s.find(digit)
            if (index == -1):
                valid = False
                break
            if (index < previous_index):
                valid = False
                break
            x_s = x_s[:index] + x_s[index+1:]
            previous_index = index
        if not valid:
            continue

        yield (i, x-i)

for _ in range(int(input())):
    #Read blank
    input()
    n = int(input())
    pairs = list(get_pairs(n))

    print(len(pairs))
    for pair in reversed(pairs):
        y,x = pair
        if (y in range(11)):
            y = "0"+str(y)
        print("%s + %s = %d" % (str(x),str(y),n))


