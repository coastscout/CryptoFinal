#2/c Joseph Church
#Collaborated w/ 2/c Felix Hernandez 

# Function to convert hexadecimal to integer
def hex_to_int(hex_value):
    return int(hex_value, 16)

# Given values in hexadecimal
e_hex = "0x10001"  
n_hex = "0x04c4540b5650fc7216f50d00b2996201"  
C_hex = "0x1b20605f40f83ac4805de9eb26b4dfa"  

# Convert hexadecimal to integer
e = hex_to_int(e_hex)
n = hex_to_int(n_hex)
C = hex_to_int(C_hex)

# Pre-compute y^e mod n for all y; keep going until e plus 2
y_powers = {pow(y, e, n): y for y in range(1, e + 2)}

# Iterate over x and check if the pre-computed y matches
for x in range(1, e + 2): #Calculate for 1 until e plus 2 
    x_inv = pow(x, -1, n)  # Modular inverse of x (mod n) Left most column
    x_final = (C * x_inv) % n  #Right most column

    if x_final in y_powers:  #Break after finding the first match
        y = y_powers[x_final] #Take the index of x_final and use that to find y
        print("Match found:")
        print("x value:", x)
        print("y value:", y)
        break  

message = x*y

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
print(decimal_to_text(message, 'utf-8'))

# If UTF-8 doesn't work, try ASCII
print(decimal_to_text(message, 'ascii'))

# Try ISO-8859-1
print(decimal_to_text(message, 'iso-8859-1'))