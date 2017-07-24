#!/bin/env python

from copy import deepcopy

score_table = {3: 1,
               4: 1,
               5: 2,
               6: 3,
               7: 5}

def get_score(pos, board, curr_word, word):

    if (len(curr_word) > len(word)):
        return 0

    if (curr_word == word):
        return score_table.get(len(curr_word), 11)

    score = 0

    #Up down left right right-up right-down left-up left-down
    for direction in [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
        new_pos = (pos[0]+direction[0], pos[1]+direction[1])
        if (new_pos[0] >= 0 and new_pos[0] < 4 and
            new_pos[1] >= 0 and new_pos[1] < 4):

            new_letter = board[new_pos[1]][new_pos[0]]
            if (new_letter == word[len(curr_word)]):
                copy = deepcopy(board)
                copy[new_pos[1]][new_pos[0]] = '_'
                score = get_score(new_pos, copy, curr_word+new_letter, word)
                if (score != 0):
                    return score
    return 0
        


def get_final_score(board, words):
    score = 0

    word_found = {}
    for word in words:
        for y,line in enumerate(board):
            for x,char in enumerate(line):
                if (word in word_found):
                    break
                if char == word[0]:
                    copy = deepcopy(board)
                    copy[y][x] = '_'

                    scoreo = get_score((x,y), copy, char, word)
                    if (scoreo != 0):
                        word_found[word] = None
                    score += scoreo
    return score

def main():
    for i in range(int(input())):
        input()
        board = [[c for c in input().strip()] for _ in range(4)]
        words = [input().strip() for _ in range(int(input()))]

        score = get_final_score(board, words)
        print('Score for Boggle game #%d: %d' % (i+1, score))

main()
