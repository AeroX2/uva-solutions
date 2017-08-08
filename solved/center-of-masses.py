#!/bin/env python

import sys

def numbers():
    lines = sys.stdin.read().replace('\n',' ').split()
    for n in map(float,lines):
        yield n

def cross(p, q, r):
    return (q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]) 

#Monotone chain algorithm
#Taken from https://en.wikibooks.org/wiki/Algorithm_Implementation/Geometry/Convex_hull/Monotone_chain
def monotone(points):
    points = sorted(points)

    # Build lower hull 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenation of the lower and upper hulls gives the convex hull.
    # Last point of each list is omitted because it is repeated at the beginning of the other list. 
    return lower[:-1] + upper[:-1]

iterator = numbers()
n = next(iterator)
while (n >= 3):
    upoints = []
    for _ in range(int(n)):
        x = next(iterator)
        y = next(iterator)
        upoints.append((x,y))

    #print(upoints)
    points = monotone(upoints)
    #print(points)

    final_x = 0
    final_y = 0
    signed = 0
    for i in range(len(points)):
        x,y = points[i]
        x1,y1 = points[i+1] if i != len(points)-1 else points[0]
        snd = (x*y1-x1*y)

        final_x += (x+x1)*snd
        final_y += (y+y1)*snd
        signed += snd

        #print(final_x, final_y, signed)

    final_x /= (3*signed)
    final_y /= (3*signed)
    print('%.3f %.3f' % (final_x, final_y))

    n = next(iterator)
