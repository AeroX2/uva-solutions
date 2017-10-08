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

    if (s < 0 or r < 0 or r > 1):
        return None

    return (p1[0] + s*dx1, p1[1] + s*dy1);

def angle(p1, p2):
    a = math.atan2(p2[1]-p1[1], p2[0]-p1[0])
    if (a < 0): a += 2*math.pi
    return math.degrees(a)

def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def angle_between(n,a,b):

    close1 = math.isclose(a,n)
    close2 = math.isclose(b,n)

    condition1 = a < n or close1
    condition2 = n < b or close2

    if (a < b):
        return condition1 and condition2
    return condition1 or condition2

def cos(x):
    return math.cos(math.radians(x))

def sin(x):
    return math.sin(math.radians(x))

class Triangle:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

        self.a1 = angle(source,p1)
        self.a2 = angle(source,p2)

        self.d1 = distance(source,p1)
        self.d2 = distance(source,p2)

        if (self.a1 > self.a2): self.swap()

    def __str__(self):
        string = "Points: {} {}\n".format(self.p1,self.p2)
        string += "Angle: {} {}\n".format(self.a1,self.a2)
        string += "Distance: {} {}\n".format(self.d1,self.d2)
        return string

    def __repr__(self):
        return "{}:{}".format(self.a1,self.a2)

    def swap(self):
        self.p1,self.p2 = self.p2,self.p1
        self.a1,self.a2 = self.a2,self.a1
        self.d1,self.d2 = self.d2,self.d1

    def assign(self, other):
        self.p1 = other.p1
        self.p2 = other.p2

        self.a1 = other.a1
        self.a2 = other.a2

        self.d1 = other.d1
        self.d2 = other.d2


def raycast(source, segments):

    #Make giant diamond shaped barrier
    points = [(10,0),(0,10),(-10,0),(0,-10),(10,0)]
    triangles = []
    for i in range(1,len(points)):
        p1 = points[i-1]
        p1 = (source[0]+p1[0],source[1]+p1[1])
        p2 = points[i]
        p2 = (source[0]+p2[0],source[1]+p2[1])

        triangle = Triangle(p1,p2)
        triangles.append(triangle)
    triangles[-1].a1 = 360
    triangles[-1].swap()

    #Add every segment to the queue
    queue = []
    for segment in segments:
        segment = Triangle(segment[0],segment[1])

        angle1 = angle(segment.p1, segment.p2)
        angle2 = angle(source, segment.p1)

        if (math.isclose(angle1, angle2)):
            continue

        co = collision((source,(source[0]+1,source[1])),(segment.p1,segment.p2))
        if (co is not None and 
            not (math.isclose(co[0],segment.p1[0]) and 
                 math.isclose(co[1],segment.p1[1]))):

            segment2 = Triangle(segment.p2, co)
            segment2.a1 = 360
            segment2.swap()

            queue.append(segment2)

            segment.p2 = co
            segment.a2 = 0
            segment.d2 = distance(source,co)
            segment.swap()

        queue.append(segment)

    #print(triangles)
    print(queue)

    while (len(queue) > 0):
        segment = queue.pop()
        #print("Attempting",segment)

        for i,triangle in enumerate(triangles[::]):

            #print(triangle)

            #if (segment.a1 > triangle.a2 or math.isclose(segment.a1,triangle.a2)): continue
            if (not angle_between(segment.a1,triangle.a1,triangle.a2)):
                #print("Continuing")
                continue

            if (math.isclose(segment.a1,triangle.a2)): 
                #print("Continuing2")
                continue

            if (not math.isclose(segment.a1,triangle.a1)):
                tri = triangle_beginning_cut(segment,triangle)
                #print(triangles)
                triangles.insert(i, tri)
                #print(triangles)

            longer = False
            if (segment_same(segment, triangle)):
                #print("Its the same!")
                pass
            elif (segment_longer(segment,triangle)):
                #print("Longer")
                longer = True

                seg = segment_cut(segment,triangle)
                print("Appending segment", seg)
                queue.append(seg)
            elif (segment_shorter(segment,triangle)):
                #print("Shorter")
                longer = False

                #print(triangles)
                tri = triangle_cut(segment,triangle)
                triangles.insert(i+2, tri)
                #print(triangles)

            condition1 = segment.d1 < triangle.d1
            condition2 = segment.d2 < triangle.d2
            condition3 = math.isclose(segment.d1,triangle.d1)
            condition4 = math.isclose(segment.d2,triangle.d2)

            if ((condition1 or condition3) and 
                (condition2 or condition4)):
                triangle.assign(segment)
            #elif (~(condition1 ^ condition2)):
            #    #This is where the lines cross and be a pain
            #    print("Condition activated")

            break
        #print(triangles)
        #print(queue)

    print("Done")

    #Hack
    triangles = sorted(triangles, key=lambda x: x.a1)

    print(triangles)
    for triangle in triangles:
        print(triangle)

    area = 0
    for triangle in triangles:
        difference = triangle.a2 - triangle.a1; 
        area += 0.5 * sin(difference) * triangle.d1 * triangle.d2

    return area

def segment_same(segment, triangle):
    return (math.isclose(segment.a1,triangle.a1) and 
            math.isclose(segment.a2,triangle.a2))

def segment_longer(segment, triangle):
    return segment.a2 > triangle.a2

def segment_shorter(segment, triangle):
    return segment.a2 < triangle.a2

def segment_cut(segment, triangle):
    print("Cutting the segment")
    print(segment)
    print(triangle)

    co = collision((source,triangle.p2),(segment.p1,segment.p2))
    seg = Triangle(co, segment.p2)
    if (math.isclose(segment.a2,360)): 
        seg.a1 = 360
        seg.swap()

    segment.p2 = co
    segment.a2 = angle(source,co)
    segment.d2 = distance(source,co)

    print("Results")
    print(segment)
    print(seg)
    print()

    return seg

def triangle_cut(segment, triangle):
    print("Cutting the triangle")
    print(segment)
    print(triangle)

    co = collision((source,segment.p2),(triangle.p1,triangle.p2))

    tri = Triangle(co, triangle.p2)
    if (math.isclose(triangle.a2,360)): 
        tri.a1 = 360
        tri.swap()
    
    triangle.p2 = co
    triangle.a2 = angle(source,co)
    triangle.d2 = distance(source,co)

    print("Results")
    print(triangle)
    print(tri)
    print()

    return tri

def triangle_beginning_cut(segment, triangle):
    print("Cutting the beginning of the triangle")
    print(segment)
    print(triangle)

    co = collision((source,segment.p1),(triangle.p1,triangle.p2))

    tri = Triangle(co, triangle.p1)
    #if (math.isclose(triangle.a2,360)): 
    #    tri.a1 = 360
    #    tri.swap()

    triangle.p1 = co
    triangle.a1 = angle(source,co)
    triangle.d1 = distance(source,co)

    print("Results")
    print(triangle)
    print(tri)
    print()

    return tri

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

        barriers = []
        barriers.append((territory[-1],territory[0]))
        for i in range(1,nverts):
            barriers.append((territory[i-1],territory[i]))

        for _ in range(nbarriers):
            x1,y1,x2,y2 = map(float, next(iterator))
            barriers.append(((x1,y1),(x2,y2)))

        global source
        source = radiation

        total_area = abs(area(territory))
        area_covered = raycast(radiation, barriers);

        print("Total",total_area)
        print("Area covered", area_covered)
        print("%.3f%%" % (area_covered/total_area*100))

        line = next(iterator)

main()
