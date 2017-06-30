
case = 1
n = int(input())
while (n != 0):
    events = list(map(int,input().split()))
    count = events.count(0)
    print("Case %d: %d" % (case,(len(events)-count) - count))

    case += 1
    n = int(input())
