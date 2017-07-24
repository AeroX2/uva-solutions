#!/bin/env python

import math

def check_correct(parties, input_string):
    operator_found = ''
    operator_index = 0
    for operator in ['<=','>=','<','>','=']:
        if (input_string.find(operator) != -1):
            operator_found = operator
            operator_index = input_string.index(operator)
            break
    
    parties_in_string = [party.strip() for party in input_string[:operator_index].split('+')]
    #print(parties_in_string)

    #percentage_sum = Decimal(0)
    #for party in parties_in_string:
    #    percentage_sum += parties[party]
     
    percentage_sum = sum(parties[party] for party in parties_in_string)
    #print(percentage_sum)

    num = float(input_string[operator_index+len(operator_found):])
    larger = percentage_sum > num
    equal = math.isclose(num, percentage_sum)

    if (operator == '<='):
        return not larger or equal
        #return compare == -1 or compare == 0
    elif (operator == '>='):
        return larger or equal
        #return compare == 1 or compare == 0
    elif (operator == '<'):
        return not larger and not equal
        #return compare == -1
    elif (operator == '>'):
        return larger and not equal
        #return compare == 1
    elif (operator == '='):
        return equal

    #What
    assert False

def main():
    p,g = map(int, input().split())

    parties = {}
    for _ in range(p):
        party,percentage = input().split()
        parties[party] = float(percentage)

    for i in range(g):
        correct = check_correct(parties,input())
        print('Guess #%d was %s.' % (i+1, 'correct' if correct else 'incorrect'))

main()
