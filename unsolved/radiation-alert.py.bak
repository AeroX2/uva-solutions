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
        if (s < 0 or r < 0 or r > 1):
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

def isbetween(a,b,c):
    d1 = distance(a,c)
    d2 = distance(c,b)
    d3 = distance(a,b)
    c1 = math.isclose(d1+d2,d3)
    if (math.isclose(d1,0) or
        math.isclose(d2,0) or
        math.isclose(d3,0)):
        return False
    return c1


def raycast(source, segments):

    temp = []
    for s1 in segments:
        if (isbetween(s1[0], s1[1], source)):
            temp.append(s1)

    for s1 in temp:
        segments.remove(s1)

    points = set([p for segment in segments for p in segment])

    #Hack for evil intersecting barriers
    for s1 in segments:
        for s2 in segments:
            intersection = collision(s1,s2,False)
            if (intersection is not None):
                points.add((intersection[0], intersection[1], True))

                if intersection in points:
                    points.remove(intersection)

    previous_distance = None
    intersections = []
    for point in clockwise(source,points):

        closest_intersections = []

        #Hack check if point is a evil intersecting barrier
        for segment in segments:
            intersection = collision((source,point),segment)
            if (intersection is not None):
                #print("Ray cast success", point, segment);
                #print("Intersection", intersection);
                closest_intersections.append(intersection)


            #if (distance(source, intersection) < distance(source, closest_intersection)):

        if point in closest_intersections: closest_intersections.remove(point)
        closest_intersections = sorted(closest_intersections, key=lambda x: distance(source, x))
        print(closest_intersections)
        print(len(closest_intersections))

        #If there is no segment between radiation and the point append the point
        #Else check if the intersection point is further than the point 
        if (len(closest_intersections) <= 0):
            intersections.append(point)
            previous_distance = distance(source, point)
        elif (distance(source,closest_intersections[0]) >= distance(source,point)):

            #Hack check which point is closer to the previous point if they
            #were aligned along the source axis
            closest_distance = distance(source,closest_intersections[0])
            point_distance = distance(source,point)

            if (previous_distance is not None):
                a = abs(previous_distance - closest_distance)
                b = abs(previous_distance - point_distance)

            if (previous_distance is None or a<b):
                intersections.append(closest_intersections[0])
                intersections.append(point)
                previous_distance = point_distance
            else:
                intersections.append(point)
                intersections.append(closest_intersections[0])
                previous_distance = closest_distance

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
        #print("Distance1",distance1)
        #print("Distance2",distance2)
        #print("Angle",difference*180/math.pi)

        area += 0.5 * math.sin(difference) * distance1 * distance2
        #print(area)

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

        total_area = abs(area(territory))

        barriers = []
        for _ in range(nbarriers):
            x1,y1,x2,y2 = map(float, next(iterator))
            barriers.append(((x1,y1),(x2,y2)))

        barriers.append((territory[-1],territory[0]))
        for i in range(1,nverts):
            barriers.append((territory[i-1],territory[i]))

        area_covered = raycast(radiation, barriers);
        #print("Total",total_area)
        #print("Area covered", area_covered)
        print("%.3f%%" % (area_covered/total_area*100))

        line = next(iterator)

main()
