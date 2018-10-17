amount = 0
for _ in range(int(input())):
    s = input()
    if "donate" in s:
        amount += int(s[6:])
    elif "report" in s:
        print(amount)
