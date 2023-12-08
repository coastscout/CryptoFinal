# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:23:08 2023

@author: Tester
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:53:01 2023

@author: Cowen
"""

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
#decimal_output = 22847  # Replace with your actual decimal output

# Try UTF-8
#print(decimal_to_text(decimal_output, 'utf-8'))

# If UTF-8 doesn't work, try ASCII
#print(decimal_to_text(decimal_output, 'ascii'))

# Try ISO-8859-1
#print(decimal_to_text(decimal_output, 'iso-8859-1'))

# If none work, consider the possibility of binary data or incorrect decryption

n = int("04c4540b5650fc7216f50d00b2996201", 16);
e = 65537
c = int("0x1b20605f40f83ac4805de9eb26b4dfa", 16);

a = [(x, pow(x,e,n)) for x in range(1,10000)]
b = [(y,pow(y,-e,n)*c % n) for y in range(1,10000)]

for i in a:
    for j in b:
        if i[1] == j[1]:
            print(i[0], j[0])
            l = i[0]*j[0]
            print(decimal_to_text(l, 'ascii'))
"""
Any of the pairs found, multiply together
With that number, convert to ascii
use Jo's decimal to text script
""" 

