#!/bin/env python

for i in range(int(input())):
    scores = list(map(int, input().split()))
    
    max1 = 0
    max2 = 0
    for _ in range(3):
        x = scores.pop()
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
    scores.append((max1+max2)//2)

    score = sum(scores)

    #print(score)
    grade = None
    if (score >= 90):
        grade = 'A'
    elif (score >= 80):
        grade = 'B'
    elif (score >= 70):
        grade = 'C'
    elif (score >= 60):
        grade = 'D'
    else:
        grade = 'F'

    print("Case %d: %s" % (i+1, grade))



