import re

correct = 0
while True:
    try:
        s = input()
    except:
        break

    regex = r"(\d+)\s*(-|\+)\s*(\d+)\s*=\s*(\d+)"
    match = re.match(regex, s)
    if (not match):
        continue

    a,b,c,d = match.groups()

    a = int(a)
    c = int(c)
    d = int(d)

    if (b == '+'):
        correct += 1 if a+c==d else 0
    elif (match.group(2) == '-'):
        correct += 1 if a-c==d else 0

print(correct)
    
