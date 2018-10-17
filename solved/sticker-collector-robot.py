NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

while True:
    n,a,b = map(int,input().split())
    if (n == 0 and a == 0 and b == 0):
        break

    grid = []
    for row in range(n):
        line = list(input())

        if 'N' in line:
            robot = {'y': row, 'x': line.index('N'), 'd': NORTH}
        elif 'L' in line:
            robot = {'y': row, 'x': line.index('L'), 'd': EAST}
        elif 'S' in line:
            robot = {'y': row, 'x': line.index('S'), 'd': SOUTH}
        elif 'O' in line:
            robot = {'y': row, 'x': line.index('O'), 'd': WEST}

        grid.append(line)

    stickers = 0
    commands = input()
    for command in commands:
        #print(robot['x'],robot['y'],robot['d'])

        if command == 'D':
            robot['d'] += 1
            if (robot['d'] > WEST):
                robot['d'] = NORTH
        elif command == 'E':
            robot['d'] -= 1
            if (robot['d'] < NORTH):
                robot['d'] = WEST
        elif command == 'F':
            px,py = robot['x'],robot['y']

            if (robot['d'] == NORTH):
                robot['y'] -= 1
            elif (robot['d'] == EAST):
                robot['x'] += 1
            elif (robot['d'] == SOUTH):
                robot['y'] += 1
            elif (robot['d'] == WEST):
                robot['x'] -= 1
            
            x,y = robot['x'],robot['y']
            if (x < 0):
                robot['x'] = 0
            if (x > len(grid[0])-1):
                robot['x'] = len(grid[0])-1
            if (y < 0):
                robot['y'] = 0
            if (y > len(grid)-1):
                robot['y'] = len(grid)-1

            x,y = robot['x'],robot['y']
            cell = grid[y][x]
            if (cell == '*'):
                stickers += 1
                grid[y][x] = '.'
            elif (cell == '#'):
                robot['x'] = px
                robot['y'] = py

    print(stickers)


