# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 17:53:01 2023

@author: Cowen
"""

n = int("04c4540b5650fc7216f50d00b2996201", 16);
e = 65537
c = int("0x1b20605f40f83ac4805de9eb26b4dfa", 16);

a = [(x, pow(x,e,n)) for x in range(1,10000)]
b = [(y,pow(y,-e,n)*c % n) for y in range(1,10000)]

for i in a:
    for j in b:
        if i[1] == j[1]:
            print(i[0], j[0])
"""
Any of the pairs found, multiply together
With that number, convert to ascii
use Jo's decimal to text script
""" 

