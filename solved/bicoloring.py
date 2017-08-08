#!/bin/env python

n = int(input())
while (n > 0):

    nodes = {}
    for _ in range(int(input())):
        a,b = map(int, input().split())
        if a in nodes:
            nodes[a].append(b)
        else:
            nodes[a] = [b]

        if b in nodes:
            nodes[b].append(a)
        else:
            nodes[b] = [a]

    bicolorable = True
    labels = {}

    if (len(nodes) > 0):
        first_node = list(nodes.keys())[0]
        seen = [first_node]
        stack = [first_node]
    else:
        stack = []

    while (len(stack) > 0):
        node = stack.pop()
        
        unique = set()
        for child in nodes[node]:
            if not child in seen:
                seen.append(child)
                stack.insert(0,child)

            if child in labels:
                unique.add(labels[child])

        if (len(unique) >= 2):
            bicolorable = False
            break

        if (len(unique) == 0):
            labels[node] = False
        else:
            labels[node] = not list(unique)[0]

    if (bicolorable):
        print("BICOLORABLE.")
    else:
        print("NOT BICOLORABLE.")

    n = int(input())


