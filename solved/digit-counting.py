for _ in range(int(input())):
    s = ''
    for i in range(1,int(input())):
        s += str(i)
    print(' '.join([str(s.count(str(i))) for i in range(10)]))
