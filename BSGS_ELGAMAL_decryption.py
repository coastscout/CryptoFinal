# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:08:37 2023

@author: Cowen
"""
import math
p = int("0x60522d1", 16)
alpha = int("0x2", 16)
beta = int("0x4d51a66", 16)
t = int("0x4bba10", 16) 
r = int("0x1d624e1", 16)
k = int(math.sqrt(p))

x = [(i, pow(alpha,i,p)) for i in range(0,k)]
y = [(j, pow(alpha,-k*j,p)*beta % p) for j in range(0,k)]

for g in x:
    for h in y:
        if g[1] == h[1]:
            print(g[0], h[0])
"""a = 1633 + k*3

pow(alpha, a, p)
Out[21]: 81074790

pow(alpha, a, p) == beta
Out[22]: True 
d = t*pow(r,-a,p) % p
"""


"""
18565 - 1
18564/2 = 9282
9282/2 = 4641
b0 = pow(66,int(m),18565)
b1 = pow(b0,2,18565)
b2 = pow(b1,2,18565)
"""