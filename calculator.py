"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math
try:
    def square_root(a):
        return math.sqrt(a)
except ValueError as e:
    print(str(e))
except:
    print("Unexpected error:", sys.exc_info()[0])
try:
    def hypotenuse(a, b):
        a=abs(a)
        b=abs(b)
        math.hypot(a, b)
except:
    print("Unexpected error:", sys.exc_info()[0])



def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero")
    else:
        return a/b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Base must be positive and not equal to 1, and argument must be positive.")
    else:
        return math.log(b,a)

def exp(a, b): return a**b



