#!/bin/env python

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

    mst = set()
    for edge in sorted(edges):
        _,parent,child = edge
        if (find(parents, parent) != find(parents, child)):
            union(parents, ranks, parent, child)
            mst.add(edge)

    return mst,parents

def main():
    for _ in range(int(input())):
        node_len,road_len = map(int,input().split())

        nodes = range(1, node_len+1)

        edges = []
        for _ in range(road_len):
            parent,child,cost = map(int,input().split())
            edges.append((-cost,parent,child))

        mst,parents = kruskals(nodes, edges)

        cost = filter(lambda x: x not in mst, edges)
        cost = map(lambda x: -x[0], cost)
        print(sum(cost))

main()
