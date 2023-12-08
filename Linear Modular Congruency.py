# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:25:09 2023

@author: Adam
"""

from math import gcd
# set up these numbers

a = 264 #has the x 
b = 428
m = 364   #Mod 

a = a % m
b = b % m
# Check if gcd(a, m) = 1
c = gcd(a,m)

#print(c)

a= a/c
b= b/c
m = m/c

#print(a)
#print(b)
#print(m)

m = int(m)
a = int(a)
b = int(b)

d = pow(a,-1,m)

#print(d)

e = b*d % m
#print(e)

for i in range(0,c):
    print(e+m*i)

"""

d = pow(c,-1, m)

e = b/d % m 

print(e)

"""

"""
pow(c,-1,)

    # Calculate the modular inverse of a modulo m
a_inverse = pow(a, -1, m)
    
    # Calculate the solution
x = (c * b) % m
    
print(f"The solution for x is: {x}")
"""