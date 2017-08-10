#!/bin/env python

import sys
import math

def lines():
    lines = sys.stdin.read().split('\n')
    for line in lines:
        yield line.split()
    yield None

def area(points):
    signed = 0
    for i in range(len(points)):
        x,y = points[i]
        x1,y1 = points[i+1] if i != len(points)-1 else points[0]
        snd = (x*y1-x1*y)
        signed += snd
    return signed/2

def collision(s1, s2):
    p1,p2 = s1
    p3,p4 = s2
    denominator = ((p4[1] - p3[1]) * (p2[0] - p1[0]) - (p4[0] - p3[0]) * (p2[1] - p1[1]));
    if (denominator == 0):
        return None

    s = ((p4[0] - p3[0]) * (p1[1] - p3[1]) - (p4[1] - p3[1]) * (p1[0] - p3[0]))/denominator
    return (p1[0] + s * (p2[0] - p1[0]), p1[1] + s * (p2[1] - p1[1]));

def angle(p1, p2):
    a = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    if (a < 0): a += 2*math.pi
    return a

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def clockwise(source, segments):
    points = [p for segment in segments for p in segment]
    print(points)
    return sorted(points, key=lambda x: angle(source, x))

def raycast(source, segments):
    area = 0;
    previous_point = None

    for point in clockwise(source, segments):
        for segment in segments:
            #There should be 2 intersections, one at the wall and one at the point
            #If the wall is before the point we ignore it

            intersection2 = collision((source,point),segment)
            if (intersection2 is None):
                continue
            if (distance(source,point) < distance(source,intersection2)):
                previous_point = intersection2
                continue

            if (previous_point is None): previous_point = intersection2
            else:
                angle1 = angle(source, previous_point)
                angle2 = angle(source, intersection2)
                distance1 = distance(source, previous_point)
                distance2 = distance(source, intersection2)

                difference = abs(angle1 - angle2) % 2*math.pi;
                if (difference > math.pi): difference = 2*math.pi - difference
                print(difference)

                area += math.sin(difference) * distance1 * distance2
                previous_point = intersection2

    return area

def main():
    iterator = lines()
    line = next(iterator)
    while (line):
        nverts, nbarriers = map(int, line)
        radiation = tuple(map(float, next(iterator)))

        territory = []
        for _ in range(nverts):
            x,y = map(float, next(iterator))
            territory.append((x,y))

        total_area = area(territory)

        barriers = []
        for _ in range(nbarriers):
            x1,y1,x2,y2 = map(float, next(iterator))
            barriers.append(((x1,y1),(x2,y2)))

        barriers.append((territory[-1],territory[0]))
        for i in range(1,nverts):
            barriers.append((territory[i-1],territory[i]))

        area_covered = raycast(radiation, barriers);
        print("%.3f" % (total_area/area_covered*100))

        line = next(iterator)

main()
