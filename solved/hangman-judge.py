#!/bin/env python

n = int(input())
while (n != -1):

    wrong = {}
    curr_word = input()
    for c in input():
        if (c in curr_word):
            curr_word = [x for x in curr_word if x != c]
            if (len(curr_word) == 0):
                break
        else:
            wrong[c] = None
            if (len(wrong) >= 7):
                break

    print("Round %d" % n)
    if (len(curr_word) == 0):
        print("You win.")
    elif (len(wrong) >= 7):
        print("You lose.")
    else:
        print("You chickened out.")

    n = int(input())


