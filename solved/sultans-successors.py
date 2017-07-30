#!/bin/env python

from math import cos,sin,radians

fundamental_solutions = [
        "1f,2a,3e,4b,5h,6c,7g,8d",
        "1a,2f,3h,4c,5g,6d,7b,8e",
        "1a,2e,3h,4f,5c,6g,7b,8d",
        "1b,2e,3g,4a,5c,6h,7f,8d",
        "1b,2e,3g,4d,5a,6h,7f,8c",
        "1b,2f,3a,4g,5d,6h,7c,8e",
        "1b,2f,3h,4c,5a,6d,7g,8e",
        "1b,2g,3c,4f,5h,6e,7a,8d",
        "1b,2g,3e,4h,5a,6d,7f,8c",
        "1c,2e,3h,4d,5a,6g,7b,8f",
        "1c,2f,3b,4e,5h,6a,7g,8d",
        "1c,2e,3b,4h,5a,6g,7d,8f"]

def read_fundamentals():
    fundamentals = []
    for solution in fundamental_solutions:
        fundamentals.append([])
        for pos in solution.split(","):
            x = "abcdefgh".index(pos[1])
            y = int(pos[0])-1
            fundamentals[-1].append((x,y))

    return fundamentals

def generate_solutions(fundamentals):
    possiblities = []
    for i,angle in enumerate([0,90,-90,180]):
        angle = radians(angle)
        for solution in fundamentals:
            possiblities.append([])
            possiblities.append([])
            possiblities.append([])
            for x,y in solution:
                tx = x
                ty = y
                x = (3.5 + (x-3.5)*cos(angle) - (y-3.5)*sin(angle))
                y = (3.5 + (tx-3.5)*sin(angle) + (y-3.5)*cos(angle))

                x = round(x)
                y = round(y)

                possiblities[-1].append((x,y))
                possiblities[-2].append((7-x,y))
                possiblities[-3].append((x,7-y))

    possiblities.extend([[(7-x,y) for x,y in solution] for solution in fundamentals])
    possiblities.extend([[(x,7-y) for x,y in solution] for solution in fundamentals])

    return possiblities

def main():
    fundamentals = read_fundamentals()
    #print(fundamentals)
    possible_solutions = generate_solutions(fundamentals)
    #print(possible_solutions)

    for _ in range(int(input())):
        board = [[int(x) for x in input().split()] for _ in range(8)]

        max_score = 0
        max_solution = None
        for solution in possible_solutions:
            score = 0
            for x,y in solution:
                score += board[y][x]
            max_score = max(max_score,score)
        print('%5s' % max_score)

main()
