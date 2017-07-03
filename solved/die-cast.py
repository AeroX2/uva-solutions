#!/bin/env python

def flood_fill_x(grid, curr_pos):

    stars = []
    seen = []
    stack = [curr_pos]

    while (len(stack) > 0):
        pos = stack.pop()
        grid[pos[1]][pos[0]] = '.'

        for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
            new_pos = (pos[0]+direction[0], pos[1]+direction[1])
            if (new_pos[0] < 0 or new_pos[0] > len(grid[0])-1):
                continue
            if (new_pos[1] < 0 or new_pos[1] > len(grid)-1):
                continue

            if (new_pos in seen):
                continue
            seen.append(new_pos)

            c = grid[new_pos[1]][new_pos[0]]
            if (c == 'X'):
                stack.append(new_pos)
            elif (c == '*'):
                stars.append(new_pos)

    return stars

def flood_fill(grid, curr_pos, test):
    count = 0

    seen = []

    stack = [curr_pos]
    for x in test:
        stack.append(x)

    while (len(stack) > 0):
        pos = stack.pop()
        grid[pos[1]][pos[0]] = '.'

        for direction in [(0,1),(0,-1),(-1,0),(1,0)]:
            new_pos = (pos[0]+direction[0], pos[1]+direction[1])
            if (new_pos[0] < 0 or new_pos[0] > len(grid[0])-1):
                continue
            if (new_pos[1] < 0 or new_pos[1] > len(grid)-1):
                continue

            if (new_pos in seen):
                continue
            seen.append(new_pos)

            c = grid[new_pos[1]][new_pos[0]]

            if (c == 'X'):
                count += 1
                stars = flood_fill_x(grid, new_pos)
                for star in stars:
                    stack.append(star)
            elif (c == '*'):
                stack.append(new_pos)

    return count


throw = 1
a,b = map(int,input().split())
while (a != 0 and b != 0):
    grid = []
    for _ in range(b):
        grid.append(list(input().strip()))

    dices = []
    for i,line in enumerate(grid):
        while ('*' in line or 'X' in line):
            if ('*' in line):
                dices.append(flood_fill(grid, (line.index('*'),i), []))
            else:
                test = flood_fill_x(grid, (line.index('X'),i))
                if (len(test) > 0):
                    dices.append(flood_fill(grid, test[0], test[1:])+1)
                else:
                    dices.append(1)

    print("Throw %d" % throw)
    print(' '.join(map(str,sorted(dices))))
    print()

    throw += 1
    a,b = map(int,input().split())


