#!/bin/env python

import math
from heapq import heappop, heappush

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def shortest_path(start, end, nodes):

    dist = {}
    prev = {}
    for node in nodes:
        if (node != start):
            dist[node] = float("inf")
            prev[node] = None
    dist[start] = 0

    queue = [(0,start,[start])]
    while (len(queue) > 0):
        cost,node,path = heappop(queue)

        if (node == end):
            print(path)

        for other_node in nodes:
            if (other_node == node): continue

            #print(node, other_node)
            cost = dist[node] + distance(node,other_node)
            if (cost < dist[other_node]):
                dist[other_node] = cost
                prev[other_node] = node
                if (other_node not in queue):
                    heappush(queue,(cost,other_node,path+[other_node]))

    print(prev)
    return dist
         
def main():
    i = 0
    n = int(input())
    while (n > 0):
        stones = []
        for _ in range(n):
            x,y = map(float,input().split())
            stones.append((x,y))

        freddy = stones[0]
        fiona = stones[1]

        distance = shortest_path(freddy, fiona, stones)
        print(distance)

        distance = filter(lambda x: x != 0, distance.values())
        min_distance = min(distance)

        print('Scenario #%d' % (i+1))
        print('Frog distance = %.3f' % min_distance)
        print()

        i += 1
        input()
        n = int(input())

main()
