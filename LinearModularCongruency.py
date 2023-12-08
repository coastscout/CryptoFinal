# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 09:13:52 2023

@author: Tester
"""

#linear modular congruency

#----------------------------------------------------------------------
def findSolutions(a, b, c): # ax = b (mod c)

    x = 0
    
    while (x < c):
        
        #print("x: ", x)
        left = (a*x) % c
        right = b % c
        #print("\na*x mod c: ", left)
        
        if (left == right):
            print("\nsolution: ", x)
        
        x+=1


#--------------------------------------------------------------------

def main():
    
    findSolutions(264, 428, 364) #put in values here
    
main()