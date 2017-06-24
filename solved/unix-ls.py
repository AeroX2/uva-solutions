#!/bin/env python

from math import ceil
import sys

def input_iterator():
    for line in sys.stdin.read().strip().split('\n'):
        yield line

iterator = input_iterator();
for line in iterator:
    files = []
    max_length = 0
    
    for _ in range(int(line)):
        filei = next(iterator)
        max_length = max(max_length, len(filei))
        files.append(filei)
    max_length += 2
    files = sorted(files)

    columns = 60 // max_length
    columns += 1 if columns == 0 else 0

    print('-'*60)
    rows = ceil(len(files) / columns)
    for i in range(rows):
        for ii in range(columns):
            format_string = '%-'+str(max_length)+'s'
            if (i+rows*ii < len(files)):
                print(format_string % (files[i+rows*ii]),end='')
        print()
