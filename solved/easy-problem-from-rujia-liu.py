while True:
    try:
        _,queries = map(int,input().split())
    except:
        break

    array = list(map(int,input().split()))

    values = {}
    for i,n in enumerate(array):
        if n in values:
            values[n].append(i)
        else:
            values[n] = [i]

    for _ in range(queries):
        k,v = map(int,input().split())
        try:
            print(values[v][k-1]+1)
        except:
            print(0)

    

