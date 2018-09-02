# -*- coding: utf-8 -*-
"""
Created on Wed Aug 08 09:33:25 2018

@author: Mona
"""

def jug(jug1, jug2):
    total = jug1+jug2
    print("\t%d\t\t\t%d" % (jug1, jug2))
    if jug1 is req:
        return
    elif jug1==0:
        jug(cap1, jug2)
    elif (jug1 == cap1 and jug2<cap2):
        jug((total-cap2),cap2)
    elif jug2>0:
        jug(jug1,0)
    elif ((total<=cap2) and (jug1>=0)): 
        jug(0,total)
    
cap1 = 4
cap2 = 3
req = 2  
print("\n in %d gallon jug\t in %d gallon jug"% (cap1,cap2))
jug(0, 0)
