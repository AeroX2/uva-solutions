#!/bin/env python

from copy import deepcopy

score_table = {3: 1,
               4: 1,
               5: 2,
               6: 3,
               7: 5}
#words_found = {}
def get_score(pos, board, curr_word, word):
    #print(pos)
    #print(curr_word)
    #print(word)
    #for line in board:
    #    print(line)
    #print()

    if (len(curr_word) > len(word)):
        return 0

    if (curr_word == word):
        #print("Word found", curr_word)
        #words.remove(curr_word)
        #print("Words left", words)
        return score_table.get(len(curr_word), 11)


    score = 0
    #if (curr_word not in words_found and

    #Up down left right right-up right-down left-up left-down
    for direction in [(0,1), (0,-1), (-1,0), (1,0), (1,1), (1,-1), (-1,1), (-1,-1)]:
        new_pos = (pos[0]+direction[0], pos[1]+direction[1])
        #print(new_pos, curr_word)
        if (new_pos[0] >= 0 and new_pos[0] < 4 and
            new_pos[1] >= 0 and new_pos[1] < 4):

            new_letter = board[new_pos[1]][new_pos[0]]

            #n_letters = lambda x: x[len(curr_word):len(curr_word)+1]
            #letter_list = list(map(n_letters, words))
            #print(new_letter, 'heeeyyy')
            #print(letter_list)
            #for word in words:
            #    if (len(word) <= len(curr_word)):
            #        continue

                #if (new_letter == word[len(curr_word)]):

            if (new_letter == word[len(curr_word)]):
                copy = deepcopy(board)
                copy[new_pos[1]][new_pos[0]] = '_'
                score = get_score(new_pos, copy, curr_word+new_letter, word)
                if (score != 0):
                    return score
    return 0
        


def get_final_score(board):
    score = 0

    test = {}

    global words
    for word in words:
        for y,line in enumerate(board):
            for x,char in enumerate(line):
                if (word in test):
                    break
                if char == word[0]:
                    copy = deepcopy(board)
                    copy[y][x] = '_'
                    #print("Calling with", char)
                    temp = words[:]
                    words = [x for x in words if x[0] == char]
                    scorei = get_score((x,y), copy, char, word)
                    if (scorei != 0):
                        test[word] = None
                    score += scorei
                    words = temp
    return score

def remove_crap(board):
    letter_count = {}
    for line in board:
        for letter in line:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    #print(letter_count)

    try:
        for word in words:
            if (word):
                continue
            for letter in set(word):
                #print(word.count(letter), 'yeeee')
                if (word.count(letter) > letter_count[letter]):
                    #print("Remove", word)
                    words.remove(word)
                    break
    except:
        print("gggg")
    #print(words)
    return words


words = []
def main():
    for i in range(int(input())):
        input()
        board = [[c for c in input().strip()] for _ in range(4)]

        global words
        words = [input().strip() for _ in range(int(input()))]
        words = remove_crap(board)

        #global words_found
        #words_found = {}
        score = get_final_score(board)
        print('Score for Boggle game #%d: %d' % (i+1, score))

main()
