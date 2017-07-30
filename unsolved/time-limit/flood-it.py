#!/bin/env python

from collections import deque

#TODO The code is too slow even with caching, I need to figure out a smarter method
directions = [(0,1),(0,-1),(-1,0),(1,0)]

def valid_pos(grid, cell, direction):
    pos = (cell[0]+direction[0], cell[1]+direction[1])
    if (pos[0] < 0 or pos[0] > len(grid)-1):
        return False,False
    if (pos[1] < 0 or pos[1] > len(grid)-1):
        return False,False
    if (grid[cell[1]][cell[0]] == grid[pos[1]][pos[0]]):
        return pos,True
    return pos,False

def finished(grid):
    return len(set([j for i in grid for j in i])) == 1

def replace_color(grid, flooded, new_color):

    new_grid = [row[:] for row in grid]
    flooded = deque(flooded)
    new_cells = flooded.copy()

    while (flooded):
        cell = flooded.pop()
        #print("Cell", cell)
        #Set the cell to the new color
        new_grid[cell[1]][cell[0]] = new_color

        #print(grid)

        #Find all the other cells
        for direction in directions:
            pos,same_color = valid_pos(new_grid, cell, direction)
            if not pos or not same_color:
                #print("InValid", cell, pos, "Because %s" % ("POS" if not pos else "COL"))
                continue;
            if not pos in new_cells:
                flooded.append(pos)
                new_cells.append(pos)

    #print(new_cells, "New")
    return new_grid, new_cells

def next_move(grid, cells, direction):
    #print(cells, "Danke")
    #print(grid)
    for cell in cells:
        #If the move is valid
        pos,same_color = valid_pos(grid, cell, direction)
        if not pos or same_color:
            #print("InValid", cell, pos, "Because %s" % ("POS" if not pos else "COL"))
            continue
        #print("Valid", cell, pos)
        #Replace all the current positions we have already filled with the new color
        yield replace_color(grid, cells, grid[pos[1]][pos[0]])

cache = {}
def flood_it(grid, cells, current_move):
    if (finished(grid)):
        
        #Cache the result
        string = ' '.join([str(j) for i in grid for j in i])
        if string in cache:
            cache[string] = min(cache[string], current_move)
        else:
            cache[string] = current_move

        return current_move
    
    #TODO Should probably change this so it is set initially
    min_moves = 10000

    #print("GRID")
    #for i in grid:
    #    print(' '.join(map(str,i)))

    #print("CELLS")
    #for i in cells:
    #    print(','.join(map(str,i)), end=' ')
    #print()

    #For every direction
    for direction in directions:
        #Calculate a new move
        new_grids = []
        for (new_grid, new_cells) in next_move(grid, cells, direction):
            string = ' '.join([str(j) for i in grid for j in i])

            new_grids.append(new_grid)

            moves = 100
            if string in cache:
                moves = cache[string]

            if (current_move < moves):
                moves = flood_it(new_grid, new_cells, current_move+1)

            min_moves = min(min_moves, moves)

    return min_moves

def main():
    n = int(input())
    while (n > 0):
        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))

        _, cells = replace_color(grid, [(0,0)], grid[0][0])

        cache = {}
        print(flood_it(grid,cells,0))
        n = int(input())
    
main()
