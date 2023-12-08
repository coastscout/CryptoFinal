# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 13:55:27 2023

@author: Juan + dom
"""

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - y * (a // b)

def extended_euclidean_solver(a, b):
    gcd, x, y = extended_gcd(a, b)
    return gcd, x, y

# Get input from the user
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

# Call the extended_euclidean_solver function
gcd, x, y = extended_euclidean_solver(a, b)

# Display the results
print(f"GCD({a}, {b}) = {gcd}")
print(f"{a}*{x} + {b}*{y} = {gcd}")
print(f"x = {x} y = {y%x}")