while True:
    try:
        numbers = map(int,input().split())
    except:
        break
    numbers = list(numbers)[1:]

    valid = True
    absolutes = set()
    for i,n in enumerate(numbers[:-1],1):
        n = abs(numbers[i]-numbers[i-1])
        
        if (n in absolutes):
            valid = False
            break
        absolutes.add(n)

    for i,n in enumerate(absolutes):
        if (i+1 != n):
            valid = False
            break

    if (valid):
        print("Jolly")
    else:
        print("Not jolly")


