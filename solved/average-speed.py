#!/bin/env python

import sys

def time_to_seconds(string):
    total_seconds = 0
    string = map(int,string.split(':')[::-1])
    for i,number in enumerate(list(string)):
        total_seconds += number * pow(60,i)
    return total_seconds

total_distance = 0
last_time = 0
last_speed = 0

string = sys.stdin.read().strip()
for line in string.split('\n'):
    line = line.split()
    
    #print(line)

    seconds = time_to_seconds(line[0])
    t_time = seconds - last_time
    d = last_speed * (t_time / 3600)
    #print(last_time, last_speed, seconds, d)
    total_distance += d

    #print(total_distance)
    #print()

    if (len(line) >= 2):
        last_speed = int(line[1])
    else:
        print("{} {:.2f} km".format(line[0], total_distance))

    last_time = seconds
