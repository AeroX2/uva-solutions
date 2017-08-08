#!/bin/env python

import sys

def next_line():
    for line in sys.stdin.read().split('\n'):
        yield line.strip()
    yield ''

iterator = next_line()
line = next(iterator)
while (line):
    amount_p = int(line)

    line = next(iterator)
    people = {}
    for person in line.split():
        people[person] = (0,0)

    for _ in range(amount_p):
        split = next(iterator).split()
        person = split[0]
        money = int(split[1])
        gifts = int(split[2])

        if (gifts > 0):
            money -= money%gifts
        else:
            money = 0

        people[person] = (money,people[person][1])

        #print(person,money)

        for i in range(gifts):
            person = split[i+3]
            temp = people[person]
            people[person] = (temp[0],temp[1]+money//gifts)

    #print(people)

    for person,v in people.items():
        print(person, v[1]-v[0])
    line = next(iterator)
    if (line != ''):
        print()
