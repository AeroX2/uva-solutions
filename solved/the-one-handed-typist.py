import re

fingers = {
        "1": "qaz",
        "2": "wsx",
        "3": "edc",
        "4": "rfvtgb",
        "5": " ",
        "6": " ",
        "7": "yhnujm",
        "8": "ik,",
        "9": "ol.",
        "10": "p;/"
}

while True:
    try:
        i,words = map(int,input().split())
    except:
        break

    cant_type = ""
    while i > 0:
        for finger in re.split('\s+',input()):
            if finger in fingers:
                cant_type += fingers[finger]
            i -= 1

    max_words = None
    while words > 0:
        for word in re.split('\s+',input()):
            valid = True
            for c in word:
                if c in cant_type:
                    valid = False
                    break
            
            if (valid):
                if (max_words is None):
                    max_words = set([word])
                elif (len(word) == len(list(max_words)[0])):
                    max_words.add(word)
                elif (len(word) > len(list(max_words)[0])):
                    max_words = set([word])
            words -= 1

    if (max_words is None):
        print(0)
    else:
        print(len(max_words))
        print('\n'.join(sorted(max_words)))





    

