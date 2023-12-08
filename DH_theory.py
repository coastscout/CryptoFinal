# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:50:04 2023

@author: Tester
"""


priv = "6535f0eada6787b0aa3cb95bc49ea762a85cd3052bee2a3a848757928ed59d345b61cc86eede9e8588898fe26372d917215e2121a6a42c058a6f792283f214b5"
    
pub = "009d55284020d7b0f1ebd217feac54da2542484391745cf075a6ed013ef34c75c90406872421a31650fd9bb8d7712e17026c37ac2808be74fe4823d403c75a30f5"
    
P = "00e8df91de64e866a94ac2fab42063f4e60cb88c20a0e52a76c2242f4ab3a59cd35cf69c1aa5f172ccbc98412aa94bed5af662f715a9c5afd8b3cbe529b17cb957"


priv_i = int(priv, 16)
pub_i = int(pub, 16)
p_i = int(P, 16)

print("priv: ", priv_i)
print("priv: ", pub_i)
print("priv: ", p_i)

g = 2

A = pow(g, priv_i, p_i)
k = hex(pow(A, 5, p_i)) #the five is our secret value

print("A: ", A)
print("k: ", k)

#f9b29f32

