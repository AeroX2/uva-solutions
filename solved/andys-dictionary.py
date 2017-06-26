#!/bin/env python

import re
import sys
import string

def input_iterator():
    for line in sys.stdin.read().strip().split('\n'):
        yield line

dictionary = set()
for line in input_iterator():
    line = line.strip().lower()

    for word in re.split('[^a-zA-Z]+', line):
        if not word:
            continue
        dictionary.add(word)

for word in sorted(dictionary):
    print(word)
