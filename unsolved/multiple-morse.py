#!/bin/env python

morse = {  '.-'  :'A','-...':'B', '-.-.':'C','-..' :'D', 
           '.'   :'E','..-.':'F', '--.' :'G','....':'H', 
           '..'  :'I','.---':'J', '-.-' :'K','.-..':'L', 
           '--'  :'M','-.'  :'N', '---' :'O','.--.':'P', 
           '--.-':'Q','.-.' :'R', '...' :'S','-'   :'T', 
           '..-' :'U','...-':'V', '.--' :'W','-..-':'X', 
           '-.--':'Y','--..':'Z' }

@profile
def generate_substrings(words):
    substrings = []
    for i in range(max_length):
        substrings.append({})
        for word in words:
            substrings[i][word[0:i+1]] = True
    return substrings

@profile
def check_new_morse_code(possible, new_morse):
    #If the new morse code in the table
    if (new_morse in morse):
        #Make a new word
        #new_word = possible[0][-1]+morse[new_morse]
        new_word = possible[0][:]
        new_word[-1] += morse[new_morse]

        #Get the end word, ie "ABC XY" = "XY" and "ABC " = ""
        #split = new_word.split()
        #word = split[-1] if split and not new_word.endswith(' ') else ''
        word = new_word[-1]

        #Check if the new word is a valid substring of the words list
        if (len(word) <= len(substrings) and word in substrings[len(word)-1]):
            #If so reset the morse code and add the new word
            #print("Adding", new_word)
            possibilities.append((new_word, ''))
    elif (len(new_morse) > 4):
        #Remove if the morse code becomes too large
        remove.append(i)

@profile
def check_new_word(possible, new_word):
    #Get the end word, ie "ABC XY" = "XY" and "ABC " = ""
    word = new_word[-1]

    #If the word is too long then remove it
    if (len(word) > len(substrings)):
        remove.append(i)
        return
    elif (word in words):
        #If a full word is found
        #print("Full word found", repr(new_word))

        if (new_morse in morse):
            x = morse[new_morse]
            if (x in substrings[0]):
                #Append the word and the new character
                possibilities.append(([new_word,x], ''))

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

    possibilities = [([''],'')]
    #print(substrings)

    #Add space for one more iteration to remove the final batch
    for c in string+' ':
        #print(possibilities)
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
    print(sum(True for x in possibilities if x[1] == ' '))
    #print(list(filter(lambda x: x[1] == '', possibilities)))
