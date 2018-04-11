# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 18:34:03 2018

@author: CX
"""

def DPknapsack_no_repetition(W,w,v):
    assert len(w)==len(v) and W>=0 and len(w)>=0 and len(v)>=0
    
    n = len(w)
    
    value = [[0]*(n+1) for i in range(W+1)]

    
    for i in range(1,n+1):
        for weight in range(1,W+1):
            value[weight][i] = value[weight][i-1]
            if w[i-1]<=weight:
                new_value = value[weight-w[i-1]][i-1]+v[i-1]
                if new_value>value[weight][i]:
                    value[weight][i]=new_value
    
    return value[W][n]

W = 10
w = [6,3,4,2]
v = [30,14,16,9]
print(DPknapsack_no_repetition(W,w,v))