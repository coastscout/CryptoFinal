# Implementation of Affine Cipher in Python

#IN TERMINAL: syntax python3 BruteForceAffineCL.py | grep CGA

# Extended Euclidean Algorithm for finding modular inverse
# eg: modinv(7, 26) = 15
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                         + ord('A')) for t in text.upper().replace(' ', '')])


# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
    modular_inverse = modinv(key[0], 26)
    if modular_inverse is not None:
        return ''.join([chr(((modular_inverse * (ord(c) - ord('A') - key[1]))
                             % 26) + ord('A')) for c in cipher])
    else:
        return ''  # Unable to decrypt with this key


# Driver Code to test the above functions
def main():
    # Get user input for the phrase to decipher
    #text = input("Enter the phrase to decipher: ").upper()
    text = "" #insert phrase to decipher here.

    # Iterate over all possible keys
    for a in range(1, 26):  # a should be coprime with 26
        modular_inverse = modinv(a, 26)

        if modular_inverse is not None:
            for b in range(26):  # b can be any integer in the range [0, 25]
                key = [a, b]

                # calling decryption function
                decrypted_text = affine_decrypt(text, key)

                print(f'Key: {key}, Decrypted Text: {decrypted_text}')


if __name__ == '__main__':
    main()
