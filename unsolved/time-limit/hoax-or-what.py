import sys
from collections import Counter

def get_input():
    for line in sys.stdin:
        yield line

g = get_input()
while True:
    n = int(next(g))
    if (n == 0):
        break

    total = 0
    hoax = Counter()
    for _ in range(n):
        numbers = map(int,next(g).split())
        next(numbers)
        for b in numbers:
            hoax[b] += 1

        a,b = min(hoax),max(hoax)
        total += b-a

        hoax[a] -= 1
        if (hoax[a] <= 0):
            del hoax[a]
        
        hoax[b] -= 1
        if (hoax[b] <= 0):
            del hoax[b]
    print(total)
        
