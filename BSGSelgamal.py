# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:14:23 2023

@author: Dominic
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 7 18:25:03 2023

@author: Dominic
"""

#chatgpt + partial LT Maxam code, idk how reliable it is

p = int('0x60522d1', 16)
alpha = int('0x2', 16)
beta = int('0x4d51a66', 16)

t = int('0x4bba10', 16)
r = int('0x1d624e1', 16)

import math

# Calculate the square root of p-1
k = int(math.sqrt(p - 1))

# Build tables x and y
x = [(i, pow(alpha, i, p)) for i in range(0, k)]
y = [(j, pow(alpha, -k * j, p) * beta % p) for j in range(0, k)]

# Find a pair (g, h) such that g[1] == h[1]
for g in x:
    for h in y:
        if g[1] == h[1]:
            print("Found matching pair:")
            print("i:", g[0], "j:", h[0])
            a = g[0] + k * h[0]
            print("a:", a)

# Verify if alpha^a == beta mod p
if pow(alpha, a, p) == beta:
    print("Verification successful.")
    m = t * pow(r, -a, p) % p
    print("Decrypted message (m):", m)
else:
    print("Verification failed.")
