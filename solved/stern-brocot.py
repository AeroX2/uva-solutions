#!/bin/env python

for _ in range(int(input())):
    left = (0,1)
    middle = (1,1)
    right = (1,0)

    for char in input():
        if char == 'L':
            temp = middle
            middle = (middle[0]+left[0], middle[1]+left[1])
            right = temp
        else:
            temp = middle
            middle = (middle[0]+right[0], middle[1]+right[1])
            left = temp
    print('%d/%d' % (middle))
