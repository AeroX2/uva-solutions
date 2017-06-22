#!/bin/env python

answers = []

amount = int(input())
while (amount != 0):
    surfaces = []
    max_space = 0
    for i in range(amount):
        line = input()
        max_space = max(max_space, line.count('X'))
        surfaces.append(line.count('X'))

    surfaces = map(lambda x: max_space - x, surfaces)
    answers.append(sum(surfaces))

    amount = int(input())

for answer in answers:
    print(answer)


