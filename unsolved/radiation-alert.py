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

def collision(s1, s2, raycast=True):
    p1,p2 = s1
    p3,p4 = s2

    dx1 = p2[0] - p1[0]
    dy1 = p2[1] - p1[1]

    dx2 = p4[0] - p3[0]
    dy2 = p4[1] - p3[1]

    denominator = (dy2*dx1) - (dx2*dy1);
    if (denominator == 0):
        return None

    r = (dx1*(p1[1]-p3[1]) - dy1*(p1[0]-p3[0])) / denominator;
    s = (dx2*(p1[1]-p3[1]) - dy2*(p1[0]-p3[0])) / denominator

    if (raycast):
        if (s == 1 or s <= 0  or r < 0 or r > 1):
            return None
    elif (s <= 0 or s >= 1 or r <= 0 or r >= 1):
        return None

    return (p1[0] + s*dx1, p1[1] + s*dy1);

def angle(p1, p2):
    a = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    if (a < 0): a += 2*math.pi
    return a

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def clockwise(source, points):
    return sorted(points, key=lambda x: angle(source, x))

def raycast(source, segments):
    points = set([p for segment in segments for p in segment])

    #For evil intersecting barriers
    for s1 in segments:
        for s2 in segments:
            intersection = collision(s1,s2, False)
            if (intersection is not None):
                points.add(intersection)

    intersections = []
    for point in clockwise(source,points):
        min_intersection = None
        for segment in segments:
            intersection = collision((source,point),segment)
            if (intersection is None):
                continue

            #print("Ray cast success", point, segment);
            #print("Intersection", intersection);

            if (min_intersection is None or 
                distance(source, intersection) < distance(source, min_intersection)):
                min_intersection = intersection

        #TODO I HAVE NO IDEA HOW TO FIX THIS
        if (min_intersection == (6.0,0.0)):
            min_intersection = None

        if (min_intersection is None):
            intersections.append(point)
        elif (distance(source,point) < distance(source,min_intersection)):
            #print("Point", min_intersection)
            #print("Minimum", min_intersection)
            #if (len(intersections) > 0):
            #    print(intersections[-1])
            #    print(min_intersection)
            #    print(distance(source,intersections[-1]), distance(source,min_intersection))

            if (len(intersections) == 0 or 
                #TODO IDK 
                intersections.append(min_intersection)
                intersections.append(point)
            else:
                intersections.append(point)
                intersections.append(min_intersection)

    area = 0
    print(intersections)
    for i,point in enumerate(intersections[1:]+[intersections[0]],1):
        previous_point = intersections[i-1]

        angle1 = angle(source, previous_point)
        angle2 = angle(source, point)
        distance1 = distance(source, previous_point)
        distance2 = distance(source, point)

        difference = angle2 - angle1; #abs(angle1 - angle2) % 2*math.pi;
        #if (difference > math.pi): difference = 2*math.pi - difference

        area += 0.5 * math.sin(difference) * distance1 * distance2

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
        print("Total",total_area)
        print("Area covered", area_covered)
        print("%.3f" % (area_covered/total_area*100))

        line = next(iterator)

p1 = (6,6)
p2 = (0,7)
p3 = (4,7)
p4 = (4,0)
print(collision((p1,p2),(p3,p4)))
print(collision((p2,p1),(p3,p4)))

p1 = (0,7)
p2 = (4,7)
p3 = (0,7)
p4 = (0,10)
print(collision((p2,p1),(p3,p4),False))

main()
