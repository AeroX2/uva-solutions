while True:
    n,n2 = map(int,input().split())
    if (n == 0 and n2 == 0):
        break

    grid = []
    for _ in range(n):
        grid.append(input())

    square = []
    for _ in range(n2):
        square.append(input())

    for _ in range(4):
        amount = 0

        for y,v in enumerate(grid[:-len(square)+1]):
            for x,_ in enumerate(v[:-len(square[0])+1]):
                valid = True
                for y2,v2 in enumerate(square):
                    if (not valid):
                        break

                    for x2,cell2 in enumerate(v2):
                        if (grid[y+y2][x+x2] != cell2):
                            valid = False
                            break

                if (valid):
                    amount += 1

        square = list(zip(*square[::-1]))
        print(amount,end=' ')
    print()

                        
