case = 1
while True:
    n = int(input())
    if (n == 0):
        break

    stacks = list(map(int,input().split()))
    total = sum(stacks)
    height = total//len(stacks)

    moves = 0
    for i,stack in enumerate(stacks):
        #print(stacks)
        while stack > height:
            lowest_stack = min(stacks)
            lowest_stack_i = stacks.index(lowest_stack)
            added_blocks = min(stack-height, height-lowest_stack)

            stacks[i] -= added_blocks
            stacks[lowest_stack_i] += added_blocks

            stack = stacks[i]
            moves += added_blocks

    print("Set #%d" % case)
    print("The minimum number of moves is %d." % moves)
    print()

    case += 1
