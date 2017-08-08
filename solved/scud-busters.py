#!/bin/env python

import sys

def numbers():
    lines = sys.stdin.read().replace('\n',' ').split()
    for n in map(float,lines):
        yield n
    yield None

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

def area(points):
    signed = 0
    for i in range(len(points)):
        x,y = points[i]
        x1,y1 = points[i+1] if i != len(points)-1 else points[0]
        snd = (x*y1-x1*y)
        signed += snd
    return signed/2

def point_in_polygon(points, test):
    inside = False
    i = 0
    j = len(points)-1
    for i in range(len(points)):
        point_i = points[i]
        point_j = points[j]
        if ( ((point_i[1]>test[1]) != (point_j[1]>test[1])) and
            (test[0] < (point_j[0]-point_i[0]) * (test[1]-point_i[1]) / (point_j[1]-point_i[1]) + point_i[0])):
            inside = not inside
        j=i
    return inside

kingdoms = []
missiles = False
total_area = 0

iterator = numbers()
n = next(iterator)
while (True):
    points_len = int(n)
    if (points_len == -1):
        missiles = True

    if (not missiles):
        points = []
        for _ in range(points_len):
            x = next(iterator)
            y = next(iterator)
            points.append((x,y))
        kingdoms.append(monotone(points))
        n = next(iterator)
    else:
        x = next(iterator)
        if (x is None):
            break
        y = next(iterator)

        for kingdom in reversed(kingdoms):
            if (point_in_polygon(kingdom, (x,y))):
                total_area += area(kingdom)
                kingdoms.remove(kingdom)
                break

print("%.2f" % total_area)
