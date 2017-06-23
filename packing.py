#!/bin/env python

for i in range(int(input())):
    print("Case %d: %s" % (i+1, "good" if all(int(x) <= 20 for x in input().split()) else "bad" ))
