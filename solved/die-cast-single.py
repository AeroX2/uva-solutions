#!/bin/env python

def flood_fill(grid, curr_pos, blub):
    count = 0

    seen = []
    stack = [(curr_pos, False)]

    while (len(stack) > 0):
        pos,not_counting = stack.pop()

        test = grid[pos[1]][pos[0]]
        if (test == '*'):
            removing_crosses = False
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

            if (not_counting):
                if (c == 'X'):
                    stack.append((new_pos, True))
                elif (c == '*'):
                    stack.insert(0,(new_pos, False))
            else:
                if (c == 'X'):
                    count += 1
                    stack.append((new_pos, True))
                elif (c == '*'):
                    stack.insert(0,(new_pos, False))

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
                dices.append(flood_fill(grid, (line.index('*'),i), False))
            else:
                dices.append(flood_fill(grid, (line.index('X'),i), True))

    print("Throw %d" % throw)
    print(' '.join(map(str,sorted(dices))))
    print()

    throw += 1
    a,b = map(int,input().split())


