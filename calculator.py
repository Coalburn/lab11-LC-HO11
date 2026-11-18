"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
def add(a, b):
    return a+b
def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    else:
        return b/a
def logarithm(a, b):
    if b<1:
        raise ValueError("Logarithm of non-positive number")
    else:
        return math.log(b, a)
def exponent(a, b):
    return a**b








