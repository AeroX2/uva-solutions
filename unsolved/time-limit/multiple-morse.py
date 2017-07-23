#!/bin/env python

morse = {  '.-'  :'A','-...':'B', '-.-.':'C','-..' :'D', 
           '.'   :'E','..-.':'F', '--.' :'G','....':'H', 
           '..'  :'I','.---':'J', '-.-' :'K','.-..':'L', 
           '--'  :'M','-.'  :'N', '---' :'O','.--.':'P', 
           '--.-':'Q','.-.' :'R', '...' :'S','-'   :'T', 
           '..-' :'U','...-':'V', '.--' :'W','-..-':'X', 
           '-.--':'Y','--..':'Z' }

def generate_substrings(words):
    substrings = []
    for i in range(max_length):
        substrings.append(set())
        for word in words:
            substrings[i].add(word[0:i+1])
    return substrings

def check_new_morse_code(possible, new_morse):
    #If the new morse code in the table
    if (new_morse in morse):
        #Make a new word
        new_word = (possible[0]+morse[new_morse])

        #Get the end word, ie "ABC XY" = "XY" and "ABC " = ""
        split = new_word.split()
        word = split[-1] if split and not new_word.endswith(' ') else ''

        #Check if the new word is a valid substring of the words list
        if (len(word) <= len(substrings) and word in substrings[len(word)-1]):
            #If so reset the morse code and add the new word
            #print("Adding", new_word)
            possibilities.append((new_word, ''))
    elif (len(new_morse) > 4):
        #Remove if the morse code becomes too large
        remove.append(i)

def check_new_word(possible, new_word):
    #Get the end word, ie "ABC XY" = "XY" and "ABC " = ""
    split = new_word.split()
    word = split[-1] if split and not new_word.endswith(' ') else ''

    #If the word is too long then remove it
    if (len(word) > len(substrings)):
        remove.append(i)
        return
    elif (word in words):
        #If a full word is found
        if (new_morse in morse):
            x = morse[new_morse]
            if (x in substrings[0]):
                print("Full word found", repr(new_word), i)
                #Append the word and the new character
                possibilities.append((x, ''))
                remove.append(i)
                generated_words.append(new_word)

for _ in range(int(input())):
    #Read blank
    input()
    string = input()

    max_length = 0
    words = {}
    for _ in range(int(input())):
        word = input()
        max_length = max(max_length, len(word))
        words[word] = True

    substrings = generate_substrings(words)

    possibilities = [('','')]
    #print(substrings)

    generated_words = []

    #Add space for one more iteration to remove the final batch
    for c in string+' ':
        print(possibilities)
        #print(len(possibilities))

        remove = []
        for i,possible in enumerate(possibilities[:]):
            #print()
            #print(possibilities)

            new_morse = possible[1]+c
            check_new_morse_code(possible, new_morse)

            new_word = possible[0]
            check_new_word(possible, new_word)
           
            #Modify the original
            possibilities[i] = (new_word, new_morse) 

        for i in reversed(remove):
            #print("Removing", possibilities[i])
            del possibilities[i]

    #print(possibilities)
    print(generated_words)
    print(sum(True for x in possibilities if x[1] == ' '))
    #print(list(filter(lambda x: x[1] == '', possibilities)))
