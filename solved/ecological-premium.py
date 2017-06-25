#!/bin/env python

for _ in range(int(input())):
    budget_sum = 0
    for _ in range(int(input())):
        size, animals, eco = map(int, input().split())  
        budget_sum += size/animals * eco * animals
    print(round(budget_sum))
