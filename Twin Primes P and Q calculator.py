# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:24:36 2023

@author: Joseph
"""

import math

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_factors(n):
    """Find the prime factors of n."""
    sqrt_n = int(math.sqrt(n))
    
    # Check if n is even
    if n % 2 == 0:
        return 2, n // 2

    # Start searching from the square root of n
    for i in range(sqrt_n, 1, -1):
        if n % i == 0 and is_prime(i):
            return i, n // i

    return None

# Given modulus n
n = 892596565691592517765051880018837

# Find prime factors
factors = find_factors(n)

if factors:
    p, q = factors
    print(f"Found prime factors: p = {p}, q = {q}")
else:
    print("Prime factors not found. Try a different method.")
