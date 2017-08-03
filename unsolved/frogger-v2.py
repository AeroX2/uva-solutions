#!/bin/env python

import math
from heapq import heappop, heappush
from collections import defaultdict

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def fake_distance(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def find(parents, vert):
    if (parents[vert] != vert):
        parents[vert] = find(parents,parents[vert])
    return parents[vert]

#@profile
def union(parents, ranks, v1, v2):
    r1 = find(parents, v1)
    r2 = find(parents, v2)
    if (r1 != r2):
        rank1 = ranks[r1]
        rank2 = ranks[r2]
        if (rank1 > rank2):
            parents[r2] = r1
        else:
            parents[r1] = r2
            if (rank1 == rank2): ranks[r2] += 1

#@profile
def kruskals(nodes, edges):
    parents = {}
    ranks = {}

    for node in nodes:
        parents[node] = node
        ranks[node] = 0

    mst = defaultdict(set)
    for edge in sorted(edges):
        _,parent,child = edge
        if (find(parents, parent) != find(parents, child)):
            union(parents, ranks, parent, child)
            mst[parent].add(child)

    return mst,parents

def depth_first(mst, curr_node, to_node, path):
    for from_node in mst[curr_node]:
        temp = distance(from_node, curr_node)
        if (from_node == to_node):
            return path

        blub = depth_first(mst, from_node, to_node, path+[(temp,from_node)])
        if (blub is not None):
            return blub

    print(curr_node)
    print(mst[curr_node])
    return None

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

        edges = []
        nodes = stones
        for node1 in nodes:
            for node2 in nodes:
                edges.append((fake_distance(node1,node2),node1,node2))

        mst,parents = kruskals(nodes, edges)
        print(mst)
        min_distance = depth_first(mst, freddy, fiona, [])
        print(min_distance)
        min_distance = min(map(lambda x: x[0], min_distance))

        print('Scenario #%d' % (i+1))
        print('Frog distance = %.3f' % min_distance)
        print()

        i += 1
        input()
        n = int(input())

main()
