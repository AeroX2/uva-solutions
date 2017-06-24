#!/bin/env python

string = input().split()
length = int(string[0])
while (length > 0):
    output = ""
    l = len(string[1]) // length
    for i in range(length):
        output += string[1][i*l:i*l+l][::-1]
    print(output)

    string = input().split()
    length = int(string[0])


