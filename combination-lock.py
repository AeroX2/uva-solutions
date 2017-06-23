#!/bin/env python
import math

def rotation(pos, des):
    distance = (pos*9 - des*9)
    if (distance < 0):
        distance = 360 + distance
    return distance

numbers = list(map(int, input().split()))
while (sum(numbers) > 0):
    total_rotation = 360*3
    total_rotation += rotation(numbers[0], numbers[1])
    total_rotation += rotation(numbers[2], numbers[1])
    total_rotation += rotation(numbers[2], numbers[3])

    print(total_rotation)
    numbers = list(map(int, input().split()))

