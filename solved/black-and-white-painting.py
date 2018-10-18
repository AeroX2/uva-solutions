import math

while True:
    a,b,c = map(int, input().split())
    if (a == 0 and b == 0 and c == 0):
        break
    
    result = ((a-7)*(b-7)) / 2

    if (c):
        print(math.ceil(result))
    else:
        print(math.floor(result))

