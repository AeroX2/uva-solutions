while True:
    try:
        n = int(input())
    except:
        break


    stack = []
    is_stack = True
    queue = []
    is_queue = True
    priority = []
    is_priority = True

    for _ in range(n):
        op,num = map(int,input().split())
        
        if op == 1:
            stack.append(num)
            queue.append(num)

            priority.append(num)
            priority = sorted(priority)

        elif op == 2:
            is_stack = is_stack and len(stack) > 0 and stack.pop() == num
            is_queue = is_queue and len(queue) > 0 and queue.pop(0) == num
            is_priority = is_priority and len(priority) > 0 and priority.pop() == num 

    z = [is_stack,is_queue,is_priority]
    z = list(filter(None,z))
    
    if (len(z) >= 2):
        print('not sure')
    elif (is_stack):
        print('stack')
    elif (is_queue):
        print('queue')
    elif (is_priority):
        print('priority queue')
    else:
        print('impossible')

