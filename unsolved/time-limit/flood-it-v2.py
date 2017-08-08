#!/bin/env python

from collections import deque

from ctypes import *

class Point(Structure):
    _fields_ = [("x", c_int), ("y", c_int)]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))

    def __str__(self):
        return "X: %d Y: %d" % (self.x,self.y)

    def __repr__(self):
        return "Point(%d,%d)" % (self.x,self.y)

#class Point:
#    def __init__(self, x,y):
#        self.x = x
#        self.y = y
#
#    def __eq__(self, other):
#        return self.x == other.x and self.y == other.y
#
#    def __hash__(self):
#        return hash((self.x,self.y))
#
#    def __str__(self):
#        return "X: %d Y: %d" % (self.x,self.y)
#
#    def __repr__(self):
#        return "Point(%d,%d)" % (self.x,self.y)

directions = [Point(0,1),Point(0,-1),Point(-1,0),Point(1,0)]

grid_width = 0
grid_height = 0

@profile
def valid_pos(x,y):
    if (x < 0 or x > grid_width):
        return False
    if (y < 0 or y > grid_height):
        return False
    return True

def same_color(grid, new_pos, cell):
    return grid[cell.y][cell.x] == grid[new_pos.y][new_pos.x]

def finished(grid):
    return len(set([j for i in grid for j in i])) == 1

@profile
def flood_find(grid, cell):
    count = 0

    global seen
    seen[cell] = None

    perimeter = []
    flooded = []
    for direction in directions:
        x = cell.x+direction.x
        y = cell.y+direction.y
        if (valid_pos(x,y)):
            new_cell = Point(cell.x+direction.x, cell.y+direction.y)
            if (new_cell in seen):
                continue

            #print(grid[new_cell.y][new_cell.x])
            if (same_color(grid, new_cell, cell)):
                #Same color
                p,f = flood_find(grid, new_cell)
                perimeter.extend(p)
                flooded.extend(f)
            else:
                #Different color
                count += 1

    if (count > 0):
        perimeter.append(cell)
    else:
        flooded.append(cell)

    return perimeter,flooded

seen = {}

@profile
def replace_color(grid, flooded, perimeter, new_color):

    new_grid = [row[:] for row in grid]

    for cell in flooded:
        new_grid[cell.y][cell.x] = new_color

    for cell in perimeter:
        new_grid[cell.y][cell.x] = new_color

    new_flooded = flooded.copy()
    new_perimeter = []

    global seen
    seen = {}
    for cell in flooded:
        seen[cell] = None
    for cell in perimeter:
        seen[cell] = None

    for cell in perimeter:
        p,f = flood_find(new_grid, cell)
        new_perimeter.extend(p)
        new_flooded.extend(f)

        for cell in f:
            seen[cell] = None
        for cell in p:
            seen[cell] = None

    #print(new_flooded, new_perimeter)

    return new_grid, new_flooded, new_perimeter

@profile
def get_valid_colors(grid, perimeter):
    cell1 = list(perimeter)[0] if len(perimeter) > 0 else Point(0,0)
    perimeter_color = grid[cell1.y][cell1.x]

    colors = set()
    for cell in perimeter:
        for direction in directions:
            x = cell.x+direction.x
            y = cell.y+direction.y
            if (valid_pos(x,y)):
                new_cell = Point(cell.x+direction.x, cell.y+direction.y)
                color = grid[new_cell.y][new_cell.x]
                if (color != perimeter_color):
                    colors.add(color)
    return colors

blub = {}

class Storage:
    def __init__(self, grid, flooded, perimeter, depth):
        self.grid = grid
        self.flooded = flooded
        self.perimeter = perimeter
        self.depth = depth

def test(grid):
    return [hash(tuple(x)) for x in grid]

@profile
def flood_it(grid, flooded, perimeter):

    s = Storage(grid, flooded, perimeter, 0)
    queue = deque([s])

    blub = []

    max_blub = 0
    while (len(queue) > 0):
        s = queue.popleft()

        #print(len(queue))

        #for x in queue:
        #    print(x.depth, end=' ')
        #print()

        #print(s.grid)
        #print(s.perimeter)
        #print(s.depth)

        blub.append(test(s.grid))

        if (finished(s.grid)):
            print(max_blub)
            return s.depth

        color_list = get_valid_colors(s.grid, s.perimeter)
        for color in color_list:
            new_grid, new_flooded, new_perimeter = replace_color(s.grid, s.flooded, s.perimeter, color)

            #if (test(new_grid) in blub):
            #    continue

            sn = Storage(new_grid, new_flooded, new_perimeter, s.depth+1)
            queue.append(sn)

        max_blub += 1

    return None

def main():
    n = int(input())
    while (n > 0):
        grid = [[int(x) for x in input().split()] for _ in range(n)]
        global grid_width
        global grid_height
        grid_width = len(grid[0])-1
        grid_height = len(grid)-1

        global seen
        seen = {}

        perimeter, flooded = flood_find(grid, Point(0,0))
        print("Ansss",flood_it(grid, flooded, perimeter))

        n = int(input())
    
main()
