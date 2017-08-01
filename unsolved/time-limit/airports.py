#!/bin/env python

#@profile
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


#@profile
#def prims(cnode, links, airport_cost):
#    total_cost = 0
#
#    visited_nodes = {}
#    visited_nodes[cnode] = None
#
#    links_left = links[cnode]
#
#    finished = False
#    while (not finished):
#        finished = True
#        for link in sorted(links_left):
#            cost,node = link
#            if (not node in visited_nodes):
#                total_cost += cost
#
#                links_left.extend(links[node])
#                links_left = list(filter(lambda x: not x[1] in visited_nodes, links_left))
#
#                visited_nodes[node] = None
#                finished = False
#                break
#
#    return visited_nodes,total_cost

#@profile
def main():
    for i in range(int(input())):
        locations, roads, airport_cost = map(int,input().split())
        #print(locations, roads, airport_cost)

        #links = {}
        #for j in range(locations):
        #    links[j+1] = []

        nodes = range(1,locations+1)

        edges = []
        for _ in range(roads):
            parent, child, cost = map(int,input().split())
            if (cost < airport_cost):
                #links[parent].append((cost, child))
                #links[child].append((cost, parent))
                edges.append((cost,parent,child))
                #edges.append((cost,child,parent))

        mst,parents = kruskals(nodes, edges)

        airports = map(lambda x: find(parents, x), parents)
        total_airports = len(set(airports))

        cost = sum(map(lambda x: x[0], mst))
        print(mst)
        total_cost = total_airports*airport_cost + cost

        print("Case #%d: %d %d" % (i+1,total_cost, total_airports))
        input()

main()
