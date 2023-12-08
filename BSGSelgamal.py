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

def decimal_to_text(decimal_input, encoding='utf-8'): 
    # Convert decimal to hex
    hex_string = format(decimal_input, 'x')

    # Ensure the hex string has an even number of characters
    hex_string = '0' + hex_string if len(hex_string) % 2 else hex_string

    # Convert hex to bytes
    bytes_data = bytes.fromhex(hex_string)

    # Try to convert bytes to string using the specified encoding
    try:
        return bytes_data.decode(encoding)
    except UnicodeDecodeError:
        return "Decoded bytes do not form a valid string in " + encoding + " encoding"

# Example usage with different encodings
decimal_output = m  # Replace with your actual decimal output

# Try UTF-8
print("UTF-8:", decimal_to_text(decimal_output, 'utf-8'))

# If UTF-8 doesn't work, try ASCII
print("ASCII:", decimal_to_text(decimal_output, 'ascii'))

# Try ISO-8859-1
print("ISO-8859-1:",decimal_to_text(decimal_output, 'iso-8859-1'))
