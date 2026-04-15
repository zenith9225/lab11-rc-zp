# https://github.com/zenith9225/lab11-rc-zp.git
# Partner 1: Zack Phillips
# Partner 2: Riley Carr

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

import math

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a

def exp(a, b):
    return a ** b

def subtract(a, b):
    return a - b

def logarithm(a, b):
    if a<=0:
        raise ValueError
    else:
        return math.log(b,a)
