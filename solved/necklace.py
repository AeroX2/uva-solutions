#!/bin/env python
import math

v_total, v_zero = map(float, input().split())
while (v_total != 0 and v_zero != 0):
    
    temp = v_total/(2*v_zero)
    if (temp.is_integer()):
        print(int(temp))
    else:
        floor = math.floor(temp)
        ceil = math.ceil(temp)

        diameter1 = 0
        if (ceil > 0): # and v_total/ceil > v_zero):
            diameter1 = ceil**2 * (v_total/ceil-v_zero)

        diameter2 = 0
        if (floor > 0): # and v_total/floor > v_zero):
            diameter2 = floor**2 * (v_total/floor-v_zero)

        if (math.isclose(diameter1,diameter2)):
            print(0)
        elif (diameter1 > diameter2):
            print(ceil)
        else:
            print(floor)

    v_total, v_zero = map(int, input().split())

