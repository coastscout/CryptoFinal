def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def find_coefficients(a, b):
    g, x, y = extended_gcd(a, b)
    return x, y

# Given coefficients from the equation 62599708x + 1658825y = 1
a = 62599708
b = 1658825

# Find the coefficients x and y
x, y = find_coefficients(a, b)

# Format the result as per the requested flag format
result = f"cga{{{x},{y}}}"

print(result)
