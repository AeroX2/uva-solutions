#!/bin/env python

from itertools import combinations

def withdraw(x, final):
    if (x == 0):
        return final

    last_coin = coins[0] 
    for coin in coins:
        if (coin > x):
            break
        last_coin = coin

    return withdraw(x%last_coin, final+[last_coin])

for _ in range(int(input())):
    input()
    coins = list(sorted(map(int, input().split())))

    max_coins = 0
    for i in range(1,len(coins)+1):
        for x in combinations(coins,i): 
            x = sum(x)
            #print("X",x)

            unique = set(withdraw(x,[]))
            #if (len(unique) > max_coins):
            #    print(coins)
            #    print(unique)
            #    print(x)
            max_coins = max(max_coins, len(unique))

    print(max_coins)

