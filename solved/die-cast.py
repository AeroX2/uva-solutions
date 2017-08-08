#!/bin/env python

def flood_fill(grid, stack, custom):
    array = []
    seen = []

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
            custom(stack, c, new_pos, array)

    return array

def dice_count(grid, curr_pos):
    def remove_crosses(stack, c, new_pos, array):
        if (c == '*'):
            array.append(new_pos)
        elif (c == 'X'):
            stack.append(new_pos)

    def remove_dice(stack, c, new_pos, array):
        if (c == '*'):
            stack.append(new_pos)
        elif (c == 'X'):
            array.append(1)
            stars = flood_fill(grid, [new_pos], remove_crosses)
            for star in stars:
                stack.append(star)

    stack = [curr_pos]
    output = 0
    if (grid[curr_pos[1]][curr_pos[0]] == 'X'):
        stack = flood_fill(grid, stack, remove_crosses)
        output += 1

    output += sum(flood_fill(grid, stack, remove_dice))
    return output
                

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
                dices.append(dice_count(grid, (line.index('*'),i)))
            else:
                dices.append(dice_count(grid, (line.index('X'),i)))
                #test = flood_fill_x(grid, (line.index('X'),i))
                #if (len(test) > 0):
                #    dices.append(flood_fill(grid, test[0], test[1:])+1)
                #else:
                #    dices.append(1)

    print("Throw %d" % throw)
    print(' '.join(map(str,sorted(dices))))
    print()

    throw += 1
    a,b = map(int,input().split())


