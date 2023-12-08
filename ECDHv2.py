# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:08:01 2023

@author: Adam
"""
def is_point_on_curve(x, y, a, b, p):
    return (y**2) % p == (x**3 + a * x + b) % p

def point_addition(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x_p, y_p = P
    x_q, y_q = Q

    if P != Q:
        m = ((y_q - y_p) * pow(x_q - x_p, -1, p)) % p
    else:
        m = ((3 * x_p**2 + a) * pow(2 * y_p, -1, p)) % p

    x_r = (m**2 - x_p - x_q) % p
    y_r = (m * (x_p - x_r) - y_p) % p

    return x_r, y_r

def scalar_multiply(k, P, a, p):
    k %= p
    result = None
    for bit in bin(k)[2:]:
        result = point_addition(result, result, a, p)
        if bit == '1':
            result = point_addition(result, P, a, p)
    return result

# Get user input for Elliptic Curve parameters
a = int(input("Enter coefficient a of the elliptic curve: "))
b = int(input("Enter coefficient b of the elliptic curve: "))
p = int(input("Enter the modulus (p) of the field: "))

# Base Point
x_base = int(input("Enter the x-coordinate of the base point: "))
y_base = int(input("Enter the y-coordinate of the base point: "))
P = (x_base, y_base)

# Secret keys
secret_alice = int(input("Enter Alice's secret key: "))
secret_bob = int(input("Enter Bob's secret key: "))

# Calculate public keys
public_alice = scalar_multiply(secret_alice, P, a, p)
public_bob = scalar_multiply(secret_bob, P, a, p)

# Calculate shared secret
shared_secret_alice = scalar_multiply(secret_alice, public_bob, a, p)
shared_secret_bob = scalar_multiply(secret_bob, public_alice, a, p)

# Output the results
print("\nElliptic Curve Diffie-Hellman Key Exchange:")
print("Base point P:", P)
print("Elliptic Curve coefficients: a={}, b={}, p={}".format(a, b, p))
print("Secret key (Alice):", secret_alice % p)
print("Secret key (Bob):", secret_bob % p)
print("Shared Secret (Alice):", shared_secret_alice)
print("Shared Secret (Bob):", shared_secret_bob)

# Verify that Alice and Bob share the same secret
assert shared_secret_alice == shared_secret_bob, "Error: Shared secrets are different!"
print("Shared secrets match!")

