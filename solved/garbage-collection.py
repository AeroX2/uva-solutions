#!/bin/env python

for _ in range(int(input())):
    max_weight, n = map(int, input().split())

    stops = []
    for _ in range(n):
        distance, weight = map(int, input().split())
        stops.append((distance, weight))

    total_distance = 0
    curr_weight = 0
    last_d = 0

    while (len(stops) > 0):
        d,w = stops[0]
        total_distance += d - last_d
        last_d = d

        if (curr_weight+w <= max_weight):
            #Pickup the garbage
            curr_weight += w  

            #If we are full, drive back to the dump
            if (curr_weight == max_weight):
                total_distance += d
                curr_weight = 0
                last_d = 0

            stops.pop(0)
        else:
            #Drive back to the dump
            total_distance += d*2
            curr_weight = 0

    print(total_distance + last_d)


