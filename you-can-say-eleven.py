#!/bin/env python

line = input().strip()
number = int(line)
while(number != 0):
    print("%s is%s a multiple of 11." % (line, "" if number % 11 == 0 else " not"))
    line = input().strip()
    number = int(line)
