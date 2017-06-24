#!/bin/env python
import math

outputs = []
numbers = list(map(int, input().split()))
while (numbers[0] != 0 or numbers[1] != 0):
    num_1 = numbers[0]
    num_2 = numbers[1]

    count = 0;
    carry = 0;
    while (num_1 != 0 or num_2 != 0):
        num_1,a = divmod(num_1, 10)
        num_2,b = divmod(num_2, 10)
        if (a+b+carry > 9):
            count+=1
            carry=int((a+b+carry)/10)
        else:
            carry=0

    print("%s carry operation%s." % ("No" if count == 0 else str(count), "s" if count > 1 else ""))
    numbers = list(map(int, input().split()))

for output in outputs:
    print(output)
    
