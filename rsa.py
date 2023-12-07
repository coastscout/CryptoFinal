def rational_to_contfrac(x, y):
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients

def contfrac_to_rational(frac):
    if len(frac) == 0:
        return (0, 1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac) - 1, -1):
        num, denom = frac[_] * num + denom, num
    return (num, denom)

def convergents_from_contfrac(frac):
    convs = []
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0: i]))
    return convs

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b // a) * x, x)

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    return (x + m) % m

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def decimal_to_ascii(decimal_number):
    hex_string = hex(decimal_number)[2:]  # Convert decimal to hex
    ascii_string = bytearray.fromhex(hex_string).decode('utf-8')
    return ascii_string

# Prompt user for n, e, and c in hexadecimal format
n_hex = input("Enter the value of n in hex: ")
e_hex = input("Enter the value of e in hex: ")
c_hex = input("Enter the value of c in hex: ")

n = int(n_hex, 16)
e = int(e_hex, 16)
c = int(c_hex, 16)

def crack_rsa(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            D = s * s - 4 * n
            if D >= 0:
                sq = isqrt(D)
                if sq * sq == D and (s + sq) % 2 == 0:
                    return d

d = crack_rsa(e, n)
print("d: " + str(d))
m = pow(c, d, n)

decimal_number = m
ascii_string = decimal_to_ascii(decimal_number)

print(ascii_string)
