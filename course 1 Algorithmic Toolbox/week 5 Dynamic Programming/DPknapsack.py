# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:47:44 2018

@author: CX
"""

def DPknapsack(W,w,v):
    assert len(w)==len(v)
    
    value= [0]*(W+1)
    n = len(w)
    
    for w_capacity in range(1,W+1):

        for j in range(n):
            if w[j]<=w_capacity:
                new_value = value[w_capacity-w[j]]+v[j]
                if new_value>value[w_capacity]:
                    value[w_capacity] = new_value
                    
    return value[W]

W = 10
w = [6,3,4,2]
v = [30,14,16,9]
print(DPknapsack(W,w,v))