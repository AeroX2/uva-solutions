#!/bin/env python

import sys

def input_iterator():
    for line in sys.stdin.read().strip().split('\n'):
        yield line
    yield ""

def interpret(ram):
    instructions = 1
    registers = [0]*10

    ins = 0
    while (ram[ins] != '100'):
        a,b,c = map(int,list(ram[ins]))

        if (a == 2):
            registers[b] = c
        elif (a == 3):
            registers[b] += c
        elif (a == 4):
            registers[b] *= c
        elif (a == 5):
            registers[b] = registers[c]
        elif (a == 6):
            registers[b] += registers[c]
        elif (a == 7):
            registers[b] *= registers[c]

        if (a >= 2 and a <= 7):
            registers[b] %= 1000
        elif (a == 8):
            registers[b] = int(ram[registers[c]])
        elif (a == 9):
            ram[registers[c]] = str(registers[b])

        if (a == 0 and registers[c] != 0):
            ins = int(registers[b])
        else:
            ins += 1

        instructions += 1
    return instructions

iterator = input_iterator()
n = int(next(iterator))
next(iterator)

for x in range(n):
    ram = ['000']*1000

    i = 0
    line = next(iterator)
    while (line):
        ram[i] = line.strip()
        line = next(iterator)
        i += 1

    print(interpret(ram))
    if (x < n-1):
        print()


