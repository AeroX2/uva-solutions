#!/bin/env python

outputs = []
amount = int(input())
while (amount != 0):
    matrix = []
    for _ in range(amount):
        line = input()
        matrix.append(list(map(int, line.split())))

    parity_row = []
    parity_col = []
    for i in range(amount):
        parity_col.append(sum([x[i] for x in matrix]))
        parity_row.append(sum(matrix[i]))
    
    list_1 = [x%2!=0 for x in parity_row]
    list_2 = [x%2!=0 for x in parity_col]
    sum_1 = sum(list_1)
    sum_2 = sum(list_2)

    #print(list_1, list_2, sum_1, sum_2)

    if (sum_1 >= 2 or sum_2 >= 2):
        outputs.append("Corrupt")
    elif (sum_1 + sum_2 == 2):
        outputs.append("Change bit (%d,%d)" % (list_1.index(True)+1, list_2.index(True)+1))
    else:
        outputs.append("OK")

    amount = int(input())

for output in outputs:
    pass
    #print(output)
