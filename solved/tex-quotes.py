#!/bin/env python
import sys

def input_iterator():
    for line in sys.stdin.read().strip().split('\n'):
        yield line

i = 0
for line in input_iterator():
    output = ""
    for char in line:
        if (char == '"'):
            output += "``" if i%2==0 else "''"
            i+=1
        else:
            output += char
    print(output)

