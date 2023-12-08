# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:53:04 2023

@author: Dominic
"""
import math

e = int('0x10001', 16)
n = int('0x2c02270df8b43e77d794c08b9395', 16)
c = int('0x1189e9bc6a5b53c521f809f24067', 16)

p = int(math.sqrt(n))

# Check if n can be represented as differences between squares
if n == (p - 1) * (p + 1):
    p = p
elif n == (p - 2) * (p + 2):
    p = p - 1
elif n == (p - 3) * (p + 3):
    p = p - 2
else:
    a = [p - 4 + i for i in range(0, 8)]
    for i in a:
        for j in a:
            if i * j == n:
                print(i, j)
                p = i
                q = j

# Verify if p and q are found
if 'p' in locals() and 'q' in locals():
    print("p:", p)
    print("q:", q)

    # Check if p * q is equal to n
    if p * q == n:
        # Calculate phi
        phi = (p - 1) * (q - 1)

        # Calculate private key (d)
        d = pow(e, -1, phi)

        # Decrypt the message
        m = pow(c, d, n)
        print("Decrypted message:", m)
    else:
        print("Error: p * q is not equal to n.")
else:
    print("Error: Unable to find valid values for p and q.")


decimal_number = m
hex_string = hex(decimal_number)[2:]  # Convert decimal to hex and remove the '0x' prefix
ascii_string = bytearray.fromhex(hex_string).decode('utf-8')

print("Decimal Number:", decimal_number)
print("Hexadecimal String:", hex_string)
print("ASCII String:", ascii_string)
