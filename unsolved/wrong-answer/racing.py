#!/bin/env python

class Road:
    def __init__(self, value, nodes):
        self.value = value
        self.nodes = nodes

    def __eq__(self, other):
        return self.nodes == other

class Node:
    def __init__(self, index):
        self.index = index
        self.roads = []

    def __hash__(self):
        return self.index

def find_link(node, previous_node, nodes, visited_nodes, visited_roads):
    if (node in visited_nodes):
        min_road = visited_roads[0]
        for road in reversed(visited_roads):
            if (road.value < min_road.value):
                min_road = road
        return True,min_road

    visited_nodes.append(node)
    for road in nodes[node].roads:
        if (previous_node != road.nodes[1]):
            link_found,link = find_link(road.nodes[1], node, nodes, visited_nodes, visited_roads+[road])
            if (link_found):
                return True,link

    return False,None 

def main():
    for _ in range(int(input())):
        node_len,road_len = map(int,input().split())

        nodes = {}
        for i in range(node_len):
            nodes[i+1] = Node(i)

        for _ in range(road_len):
            parent,child,value = map(int,input().split())
            #Bi-direction road
            road1 = Road(value, (parent, child))
            road2 = Road(value, (child, parent))

            nodes[parent].roads.append(road1)
            nodes[child].roads.append(road2)

        smallest_cut = 0
        while (True):
            link_found,road = find_link(1,-1,nodes,[],[])
            if (link_found):
                print("Link found",road.nodes)

                parent = road.nodes[0]
                child = road.nodes[1]
                nodes[parent].roads.remove((parent,child))
                nodes[child].roads.remove((child,parent))
                smallest_cut += road.value
            else:
                break

        print("Check",smallest_cut)

main()
