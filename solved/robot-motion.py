#!/bin/env python

direction = {
        'N': (0, -1),
        'E': (1, 0),
        'S': (0, 1),
        'W': (-1, 0),
        }

numbers = list(map(int, input().split()))
while (sum(numbers) > 0):
    grid = []
    for _ in range(numbers[0]):
        grid.append(list(input()))

    step = 0
    curr_pos = (numbers[2]-1, 0)
    seen = []
    while True:
        #print(seen)

        seen.append((curr_pos, step))
        next_move = direction[grid[curr_pos[1]][curr_pos[0]]] 
        curr_pos = (curr_pos[0]+next_move[0], curr_pos[1]+next_move[1])

        if (curr_pos[0] < 0 or curr_pos[0] > len(grid[0])-1 or
            curr_pos[1] < 0 or curr_pos[1] > len(grid)-1):
            print("%d step(s) to exit" % (step+1))
            break

        try:
            seen_index = list(map(lambda x: x[0], seen)).index(curr_pos)
            x = seen[seen_index]
            print("%d step(s) before a loop of %d step(s)" % (x[1], step-x[1]+1))
            break
        except ValueError:
            pass
        step += 1


    numbers = list(map(int, input().split()))

