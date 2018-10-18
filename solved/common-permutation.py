from collections import Counter

while True:
    try:
        s1 = input()
        s2 = input()
    except:
        break

    c1 = Counter(s1)
    c2 = Counter(s2)

    inter = c1 & c2
    for c in sorted(inter):
        print(c*inter[c],end='')
    print()

