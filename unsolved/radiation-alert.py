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
            if (s >= 0 and s <= 1):
                return None #(p1[0] + s*dx1, p1[1] + s*dy1, True);
            return None
    elif (s <= 0 or s >= 1 or r <= 0 or r >= 1):
        return None

    return (p1[0] + s*dx1, p1[1] + s*dy1);

def angle(p1, p2):
    a = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    if (a < 0): a += 2*math.pi
    return math.degrees(a)

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

def cos(x):
    return math.cos(math.radians(x))

def sin(x):
    return math.sin(math.radians(x))

def raycast(source, segments):
    triangles = [[0,100,90,100],
                 [90,100,180,100],
                 [180,100,270,100],
                 [270,100,360,100]]

    queue = segments
    while (len(queue) > 0):
        segment = queue.pop()

        p1 = segment[0]
        p2 = segment[1]

        a1 = angle(source, p1)
        a2 = angle(source, p2)

        d1 = distance(source, p1)
        d2 = distance(source, p2)

        if (a2<a1):
            a1,a2 = a2,a1
            d1,d2 = d2,d1
            p1,p2 = p2,p1

        for i,triangle in enumerate(triangles[::]):
            a3 = triangle[0]
            a4 = triangle[2]

            d3 = triangle[1]
            d4 = triangle[3]

            #If the segment starts in this triangle
            if (a1 >= a4): continue

            t1 = (cos(a3)*d3,sin(a3)*d3)
            t2 = (cos(a4)*d4,sin(a4)*d4)

            if (math.isclose(a2,a4)):
                pass
            #If the segment is longer, 
            #cut off extra piece and append to the queue
            elif (a2 > a4):
                print("Segment longer")

                longer = True

                co = collision((source,(cos(a4),sin(a4))), segment)
                a2 = a4
                d2 = distance(source,co) 

                print("Appending",(co,p2),"to the queue")
                queue.append((co,p2))

            #Else cut off the extra on the triangle piece 
            else: 
                print("Segment shorter")

                longer = False

                print(a3,a4)
                print(t1,t2)

                co = collision((source,p2), (t1,t2))
                triangle[0] = a2
                triangle[1] = distance(source,co) 
                a3 = triangle[0]
                d3 = triangle[1]

                print("Appending",(co,(cos(a4)*d4,sin(a4)*d4)),"to the queue")
                #queue.append((co,(cos(a4)*d4,sin(a4)*d4)))

            if (not math.isclose(a1,a3)): 
                #Ignore the beginning part of the triangle
                #t1 = (cos(a3)*d3,sin(a3)*d3)
                #t2 = (cos(a4)*d4,sin(a4)*d4)
                co = collision((source,p1), (t1,t2))
                print((source,p1), (t1,t2))

                triangle[2] = angle(source,co) 
                triangle[3] = distance(source,co) 
                a4 = triangle[2]
                d4 = triangle[3]
                #queue.append((t1,co))

            condition1 = d1 < d3
            condition2 = d2 < d4

            #If the segment is closer in both points
            #Pick the segment
            if (condition1 and condition2):
                print("Segment is closer inserting")
                triangles.insert(i+1 if longer else i,[a1,d1,a2,d2])

            #If the condition are different to each other
            #The lines cross calculate the cross point
            elif (condition1 and not condition2):
                pass
            #Else
            #Pick the triangle
            else:
                triangles.insert(i+1 if longer else i,[a3,d3,a4,d4])

            print(triangles)

            break

    print(triangles)

    area = 0
    for i,point in enumerate(triangles[1:]+[triangles[0]],1):

        angle1 = point[0]
        angle2 = point[2]
        distance1 = point[1]
        distance2 = point[3]

        difference = angle2 - angle1; 
        area += 0.5 * math.sin(difference) * distance1 * distance2

    return area

def main():
    iterator = lines()
    line = next(iterator)
    while (line):
        nverts, nbarriers = map(int, line)
        radiation = tuple(map(float, next(iterator)))

        #territory = []
        #for _ in range(nverts):
        #    x,y = map(float, next(iterator))
        #    territory.append((x,y))

        #total_area = abs(area(territory))

        barriers = []
        for _ in range(nbarriers):
            x1,y1,x2,y2 = map(float, next(iterator))
            barriers.append(((x1,y1),(x2,y2)))

        #barriers.append((territory[-1],territory[0]))
        #for i in range(1,nverts):
        #    barriers.append((territory[i-1],territory[i]))

        print(barriers)

        area_covered = raycast(radiation, barriers);
        #print("Total",total_area)
        #print("Area covered", area_covered)
        print("%.3f%%" % (area_covered/total_area*100))

        line = next(iterator)

main()
