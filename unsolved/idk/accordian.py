#!/bin/env python

def check_card(card1, card2):
    card1 = card1[0]
    card2 = card2[0]

    if (card1[0] == card2[0]):
        return True
    if (card1[1] == card2[1]):
        return True
    return False

line = input().strip()
while (line != '#'):
    cards = line.split()
    cards.extend(input().split())
    cards = list(map(lambda x: (x,1), cards))

    done = False
    while (not done):
        done = True
        remove_list = []
        for i,card in enumerate(cards[1:]):
            i+=1
            if (i-3 >= 0 and check_card(card, cards[i-3])):
                cards[i-3] = (card[0], cards[i-3][1]+1)
                remove_list.append(i)
                done = False
            elif (check_card(card, cards[i-1])):
                cards[i-1] = (card[0], cards[i-1][1]+1)
                remove_list.append(i)
                done = False

        for x in reversed(remove_list):
            cards.pop(x)

    print(cards)


    line = input().strip()

