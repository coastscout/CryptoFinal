# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:20:14 2023

@author: Adam
"""

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def find_coefficients(a, b, c):
    gcd, x, y = extended_gcd(a, b)
    
    if c % gcd != 0:
        raise ValueError("No solution exists for the given equation.")
    
    multiplier = c // gcd
    x *= multiplier
    y *= multiplier
    
    return x, y

# Coefficients for the equation 62599708x + 1658825y = 1
a = 62599708
b = 1658825
c = 1

try:
    x, y = find_coefficients(a, b, c)
    print(f"x = {x}, y = {y}")
except ValueError as e:
    print(str(e))
