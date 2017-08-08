#!/bin/env python

from decimal import *
import sys
import math


"""
Python doesn't have decimal math functions D:
Maths function code is taken directly from 
https://pypi.python.org/pypi/dmath, Authors (Brian Beck, Christopher Hesse)
"""

D = Decimal

def pi():
    getcontext().prec += 2
    lasts, t, s, n, na, d, da = 0, D(3), 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

def e():
    return exp(D(1))

def exp(x):
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s    
        i += 1
        fact *= i
        num *= x     
        s += num / fact   
    getcontext().prec -= 2        
    return +s

def cos(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 0, 0, 1, 1, 1, 1
    while s != lasts:
        lasts = s    
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign 
    getcontext().prec -= 2        
    return +s

def sin(x):
    getcontext().prec += 2
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s    
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    getcontext().prec -= 2
    return +s

def cosh(x):
    if x == 0:
        return D(1)
    
    getcontext().prec += 2
    i, lasts, s, fact, num = 0, 0, 1, 1, 1
    while s != lasts:
        lasts = s
        i += 2
        num *= x * x
        fact *= i * (i - 1)
        s += num / fact
    getcontext().prec -= 2
    return +s

def sinh(x):
    if x == 0:
        return D(0)
    
    getcontext().prec += 2
    i, lasts, s, fact, num = 1, 0, x, 1, x
    while s != lasts:
        lasts = s
        i += 2
        num *= x * x
        fact *= i * (i - 1)
        s += num / fact
    getcontext().prec -= 2
    return +s

# The version below is actually overwritten by the version using atan2 below
# it, since it is much faster. If possible, I'd like to write a fast version
# independent of atan2.
def asin(x):
    if abs(x) > 1:
        raise ValueError("Domain error: asin accepts -1 <= x <= 1")
    
    if x == -1:
        return pi() / -2
    elif x == 0:
        return D(0)
    elif x == 1:
        return pi() / 2
    
    getcontext().prec += 2
    one_half = D('0.5')
    i, lasts, s, gamma, fact, num = D(0), 0, x, 1, 1, x
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x * x
        gamma *= i - one_half
        coeff = gamma / ((2 * i + 1) * fact)
        s += coeff * num
    getcontext().prec -= 2
    return +s

# This is way faster, I wonder if there's a downside?
def asin(x):
    if abs(x) > 1:
        raise ValueError("Domain error: asin accepts -1 <= x <= 1")
    
    if x == -1:
        return pi() / -2
    elif x == 0:
        return D(0)
    elif x == 1:
        return pi() / 2
    
    return atan2(x, D.sqrt(1 - x ** 2))

# The version below is actually overwritten by the version using atan2 below
# it, since it is much faster. If possible, I'd like to write a fast version
# independent of atan2.
def acos(x):
    if abs(x) > 1:
        raise ValueError("Domain error: acos accepts -1 <= x <= 1")
    
    if x == -1:
        return pi()
    elif x == 0:
        return pi() / 2
    elif x == 1:
        return D(0)
    
    getcontext().prec += 2
    one_half = D('0.5')
    i, lasts, s, gamma, fact, num = D(0), 0, pi() / 2 - x, 1, 1, x
    while s != lasts:
        lasts = s
        i += 1
        fact *= i
        num *= x * x
        gamma *= i - one_half
        coeff = gamma / ((2 * i + 1) * fact)
        s -= coeff * num
    getcontext().prec -= 2
    return +s

# This is way faster, I wonder if there's a downside?
def acos(x):
    if abs(x) > 1:
        raise ValueError("Domain error: acos accepts -1 <= x <= 1")

    if x == -1:
        return pi()
    elif x == 0:
        return pi() / 2
    elif x == 1:
        return D(0)
    
    return pi() / 2 - atan2(x, D.sqrt(1 - x ** 2))

def tan(x):
    return +(sin(x) / cos(x))

def tanh(x):
    return +(sinh(x) / cosh(x))

def atan(x):
    if x == D('-Inf'):
        return pi() / -2
    elif x == 0:
        return D(0)
    elif x == D('Inf'):
        return pi() / 2
    
    if x < -1:
        c = pi() / -2
        x = 1 / x
    elif x > 1:
        c = pi() / 2
        x = 1 / x
    else:
        c = 0
    
    getcontext().prec += 2
    x_squared = x ** 2
    y = x_squared / (1 + x_squared)
    y_over_x = y / x
    i, lasts, s, coeff, num = D(0), 0, y_over_x, 1, y_over_x
    while s != lasts:
        lasts = s 
        i += 2
        coeff *= i / (i + 1)
        num *= y
        s += coeff * num
    if c:
        s = c - s
    getcontext().prec -= 2
    return +s

def sign(x):
    return 2 * D(x >= 0) - 1

def atan2(y, x):
    abs_y = abs(y)
    abs_x = abs(x)
    y_is_real = abs_y != D('Inf')
    
    if x:
        if y_is_real:
            a = y and atan(y / x) or D(0)
            if x < 0:
                a += sign(y) * pi()
            return a
        elif abs_y == abs_x:
            x = sign(x)
            y = sign(y)
            return pi() * (D(2) * abs(x) - x) / (D(4) * y)
    if y:
        return atan(sign(y) * D('Inf'))
    elif x < 0:
        return sign(y) * pi()
    else:
        return D(0)

def log(x, base=None):
    if x < 0:
        return D('NaN')
    elif base == 1:
        raise ValueError("Base was 1!")
    elif x == base:
        return D(1)
    elif x == 0:
        return D('-Inf')
    
    getcontext().prec += 2    
    
    if base is None:
        log_base = 1
        approx = math.log(x)
    else:
        log_base = log(base)
        approx = math.log(x, base)

    lasts, s = 0, D(repr(approx))
    while lasts != s:
        lasts = s
        s = s - 1 + x / exp(s)
    s /= log_base
    getcontext().prec -= 2
    return +s

sqrt = D.sqrt
pow = D.__pow__

"""Where my code actually begins"""

def two_args(op, a, b, prec):
    """
    Prec (precision) is not the numbers after the point but all the numbers
    So...adding ~50ish seems to get the answer accepted
    41 just makes it run ever so slightly faster
    This is a ugly hack but no one said this code has to be pretty
    """
    getcontext().prec = int(prec)+41

    result = None
    if (op == "add"):
        result = a+b
    elif (op == "sub"):
        result = a-b
    elif (op == "mul"):
        result = a*b
    elif (op == "div"):
        result = a/b
    elif (op == "pow"):
        result = a**b
    elif (op == "atan2"):
        result = atan2(a,b)
    #print(("{:."+str(prec)+"f}").format(result))
    return result

def one_args(op, a, prec):
    getcontext().prec = int(prec)+41

    result = None
    if (op == "exp"):
        result =  exp(a)
    elif (op == "ln"):
        result = log(a)
    elif (op == "sqrt"):
        result = sqrt(a)
    elif (op == "asin"):
        result = asin(a)
    elif (op == "acos"):
        result = acos(a)
    elif (op == "atan"):
        result = atan(a)
    elif (op == "sin"):
        result = sin(a)
    elif (op == "cos"):
        result = cos(a)
    elif (op == "tan"):
        result = tan(a)
    #print(("{:."+str(prec)+"f}").format(result))
    return result

def main():
    string = sys.stdin.read().strip()
    for line in string.split('\n'):
        split = line.split()

        op = split[0]
        split = list(map(Decimal,split[1:]))

        if (len(split) > 2):
            output = two_args(op, split[0], split[1], split[2])
            print(("{:."+str(split[2])+"f}").format(output))
        else:
            output = one_args(op, split[0], split[1])
            print(("{:."+str(split[1])+"f}").format(output))


main()
