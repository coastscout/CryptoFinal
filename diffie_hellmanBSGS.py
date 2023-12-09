# From qubard, edited slightly for cryptography final

import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def baby_step(alpha, beta, n):
        table = {}
        m = math.ceil(pow(n,1/2))
        for j in range(0, m):
            term = pow(alpha,j,n)
            table[term] = j
        alpha_neg = pow(modinv(alpha,n),m,n)
        y = beta
        for i in range(0, m):
            if y in table:
                return i*m + table[y]
            else:
                y = (y * alpha_neg) % n
                
g = 3 # generator
publicnum = 5 # number that alice or bob get when raising g to their secret
p = 19 # modulus

print("x is", baby_step(g,publicnum,p))
            
