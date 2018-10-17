i = 0
while True:
    s = input()
    i += 1
    if '*' in s:
        break

    print("Case %d: " % i,end='')
    if 'Hajj' in s:
        print("Hajj-e-Akbar")
    elif 'Umrah' in s:
        print("Hajj-e-Asghar")
