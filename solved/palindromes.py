#!/bin/env python
import sys

mirror = {
        'A': 'A', 'E': '3', 'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J', 
        'M': 'M', 'O': 'O', 'S': '2', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', 'Z': '5', '1': '1', '2': 'S', '3': 'E', '5': 'Z', '8': '8' }

def input_iterator():
    for line in sys.stdin.read().strip().split('\n'):
        yield line

def is_palidromes(string):
    return string[::-1] == string

def is_mirror(string):
    mirrored_string = ''
    for c in string:
        if c in mirror:
            mirrored_string += mirror[c]
        else:
            return False
    return mirrored_string[::-1] == string

for s in input_iterator():
    palidromes = is_palidromes(s)
    mirrored = is_mirror(s)
    if not palidromes and not mirrored:
        print(s, "-- is not a palindrome.")
    elif not mirrored:
        print(s, "-- is a regular palindrome.")
    elif not palidromes:
        print(s, "-- is a mirrored string.")
    else:
        print(s, "-- is a mirrored palindrome.")
    print()




