#!/bin/env python

def withdraw(x, final):
    if (x == 0):
        return final

    last_coin = coins[0] 
    for coin in coins:
        if (coin > x):
            break
        last_coin = coin

    return withdraw(x-last_coin, final+[last_coin])

for _ in range(int(input())):
    input()
    coins = list(map(int, input().split()))

    max_coins = 0
    for x in range(sum(coins)):
        max_coins = max(max_coins, len(set(withdraw(x,[]))))
    print(max_coins)


