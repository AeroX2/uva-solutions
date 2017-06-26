#!/bin/env python

import time

for _ in range(int(input())):
    _, position = map(int, input().split())
    jobs = list(map(lambda x: (int(x), False), input().split()))

    minutes = 0
    jobs[position] = (jobs[position][0], True)

    while True:
        curr_job = jobs.pop(0)

        if (len(jobs) > 0 and curr_job[0] < max(jobs, key=lambda x: x[0])[0]):
            jobs.append(curr_job)
        elif (curr_job[1]):
            break
        else:
            minutes += 1
    print(minutes+1)
