#!/bin/env python

morse_table = {  '.-'  :'A','-...':'B', '-.-.':'C','-..' :'D', 
                 '.'   :'E','..-.':'F', '--.' :'G','....':'H', 
                 '..'  :'I','.---':'J', '-.-' :'K','.-..':'L', 
                 '--'  :'M','-.'  :'N', '---' :'O','.--.':'P', 
                 '--.-':'Q','.-.' :'R', '...' :'S','-'   :'T', 
                 '..-' :'U','...-':'V', '.--' :'W','-..-':'X', 
                 '-.--':'Y','--..':'Z' }

#@profile
def generate_substrings(words, max_length):
    substrings = []
    for i in range(max_length):
        substrings.append({})
        for word in words:
            substrings[i][word[0:i+1]] = None
    return substrings

#@profile
def check_morse_code(possible, substrings, words_generated):
    morse = possible[1]

    #If the new morse code in the table
    if (morse in morse_table):
        wordp = possible[0]+morse_table[morse]

        for gen_word in words_generated:
            word = gen_word[1] + wordp
            word_len = len(word)

            #Check if the new word is a valid substring of the words list
            if (word_len <= len(substrings) and word in substrings[word_len-1]):
                #If so reset the morse code and add the new word
                #print("Adding", word)
                return (word, ''),False
    elif (len(morse) >= 4):
        #Remove if the morse code becomes too large
        return (),True
    return None,False

#@profile
def check_word(possible, substrings, words, words_generated, ci):
    wordp = possible[0]
    morse = possible[1]

    #If the word is too long then remove it
    if (len(wordp) > len(substrings)):
        return True

    if (wordp == ''):
        return False

    for gen_word in words_generated[:]:
        word = gen_word[1] + wordp
        print(word, gen_word, wordp)
        if (word in words):
            #If a full word is found
            print("Full word found", repr(word))
            words_generated.append((ci,word))
            return -1
    return False

#@profile
def generate_possiblities(string, words, substrings):

    words_generated = [(0,'')]

    possibilities = [('','')]

    for ci,c in enumerate(string+' '):
        #print(possibilities)
        #print(len(possibilities))

        remove = []
        for pi,possible in enumerate(possibilities[:]):
            print()
            print(possibilities)

            possible = (possible[0], possible[1]+c)
            possibilities[pi] = possible

            remove_possible = check_word(possible, substrings, words, words_generated, ci)
            if (remove_possible == -1):
                print("Test", possible)
                possible = ('',possible[1])
                possibilities[pi] = possible
            elif (remove_possible):
                #del possibilities[pi]
                remove.append(pi)
                continue

            new_possible, remove_possible = check_morse_code(possible, substrings, words_generated)
            if (remove_possible):
                #del possibilities[pi]
                print("Remove", possible)
                remove.append(pi)
                continue
            elif (new_possible is not None):
                possibilities.append(new_possible)


        for i in reversed(remove):
            del possibilities[i]
           
    print(words_generated)

    #print(possibilities)
    #print(total)
    return possibilities


def main():
    for _ in range(int(input())):
        #Read blank
        input()
        string = input()

        max_length = 0
        words = {}
        for _ in range(int(input())):
            word = input()
            max_length = max(max_length, len(word))
            words[word] = None

        substrings = generate_substrings(words, max_length)
        possibilities = generate_possiblities(string, words, substrings)

        print(sum(True for x in possibilities if x[1] == ' '))
        #print(list(filter(lambda x: x[1] == '', possibilities)))

main()
