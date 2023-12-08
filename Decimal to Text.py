# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:50:28 2023

@author: Joseph
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
decimal_output = 22847  # Replace with your actual decimal output

# Try UTF-8
print(decimal_to_text(decimal_output, 'utf-8'))

# If UTF-8 doesn't work, try ASCII
print(decimal_to_text(decimal_output, 'ascii'))

# Try ISO-8859-1
print(decimal_to_text(decimal_output, 'iso-8859-1'))

# If none work, consider the possibility of binary data or incorrect decryption

