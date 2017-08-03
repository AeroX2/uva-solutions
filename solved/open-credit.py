#!/bin/env python

for _ in range(int(input())):


    n = int(input())
    previous_score = int(input())

    max_difference = None
    max_mark = previous_score

    for _ in range(n-1):
        mark = int(input())

        difference = max_mark-mark

        if (max_difference is None):
            max_difference = difference
        elif (difference > max_difference):
            max_difference = difference

        if (mark > max_mark):
            max_mark = mark

    print(max_difference)

