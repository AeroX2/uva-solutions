#!/bin/env python

from collections import deque

def check_arrangement(arrangement, coaches):
    coaches = deque(coaches)
    station = deque()

    i = 0
    while (len(coaches) > 0 or len(station) > 0):
        coach_a = arrangement[i]

        if (len(station) > 0 and station[-1] == coach_a):
            station.pop()
            i += 1
        elif (len(coaches) > 0 and coaches[0] == coach_a):
            coaches.popleft()
            i += 1
        elif (len(coaches) > 0):
            station.append(coaches.popleft())
        else:
            return False

    return True

def main():
    n = int(input())
    while (n > 0):
        coaches = list(range(1,n+1))

        arrangement = [int(x) for x in input().split()]
        while (arrangement[0] > 0):

            if (check_arrangement(arrangement, coaches)):
                print("Yes")
            else:
                print("No")

            arrangement = [int(x) for x in input().split()]
        print()

        n = int(input())

main()
