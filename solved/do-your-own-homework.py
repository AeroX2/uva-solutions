import re
import math

for case in range(int(input())):

    subjects = {}
    for _ in range(int(input())):
        s = input().split() 
        subjects[s[0]] = int(s[1])

    days = int(input())
    s = input()
    if s in subjects:
        subject = subjects[s]
    else:
        subject = math.inf

    if (subject <= days):
        print('Case %d: Yesss' % (case+1))
    elif (subject <= days+5):
        print('Case %d: Late' % (case+1))
    else:
        print('Case %d: Do your own homework!' % (case+1))

