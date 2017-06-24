#!/bin/env python

import sys
from math import ceil,floor,sqrt

outputs = []
numbers = [int(x) for x in input().split()]
while (numbers[0] != 0 or numbers[1] != 0):
    print(floor(sqrt(numbers[1])) - ceil(sqrt(numbers[0]))+1)
    numbers = [int(x) for x in input().split()]
