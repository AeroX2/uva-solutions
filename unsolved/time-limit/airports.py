#!/bin/env python

#@profile
def prims(cnode, links, airport_cost):
    total_cost = 0

    visited_nodes = {}
    visited_nodes[cnode] = None

    links_left = links[cnode]

    finished = False
    while (not finished):
        finished = True
        for link in sorted(links_left):
            cost,node = link
            if (not node in visited_nodes):
                total_cost += cost

                links_left.extend(links[node])
                links_left = list(filter(lambda x: not x[1] in visited_nodes, links_left))

                visited_nodes[node] = None
                finished = False
                break

    return visited_nodes,total_cost

#@profile
def main():
    for i in range(int(input())):
        locations, roads, airport_cost = map(int,input().split())
        #print(locations, roads, airport_cost)

        links = {}
        for j in range(locations):
            links[j+1] = []

        for _ in range(roads):
            parent, child, cost = map(int,input().split())
            if (cost < airport_cost):
                links[parent].append((cost, child))
                links[child].append((cost, parent))

        #print("GG",links)

        total_cost = 0
        total_airports = 0
        stack = list(links.keys())
        while (len(stack) > 0):
            node = stack.pop()
            remove_nodes,cost = prims(node, links, airport_cost)

            #print(remove_nodes,cost)

            #for nodet in remove_nodes:
            #    if (nodet != node):
            #        #print(stack, node)
            #        stack.remove(nodet)
            stack = list(filter(lambda x: not x in remove_nodes or x == node, stack))

            total_cost += airport_cost + cost
            total_airports += 1
        print("Case #%d: %d %d" % (i+1,total_cost, total_airports))
        #input()

main()
