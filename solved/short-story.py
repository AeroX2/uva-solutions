#!/bin/env python

import sys

def page():
    for line in sys.stdin.read().split('\n'):
        yield line.strip()
    yield ''

iterator = page()
line = next(iterator)
while (line):
    _,l,c = map(int, line.split())
    input_line = next(iterator)

    line = []
    page = 0
    pages = 0

    words = input_line.split()[::-1]
    while (len(words) > 0):
        word = words.pop()

        line.append(word)
        if (len(' '.join(line)) > c):
            words.append(line.pop())
            #page.append(' '.join(line))
            page += 1
            line = []

            if (page >= l):
                pages += 1
                #pages.append(page)
                page = 0

    if (len(line) > 0):
        #pages.append(line)
        pages += 1

    #print("N",l,c)
    #print(pages)

    #for page in pages:
    #    for line in page:
    #        print(line, len(line))
    #    print()

    print(pages)

    line = next(iterator)


