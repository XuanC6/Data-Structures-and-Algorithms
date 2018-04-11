# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:25:44 2018

@author: CX
"""
import math

def minimum_distance_1d(x):
    n = len(x)
    d = float('inf')
    if n <=1:
        return d
    x.sort()
    for i in range(n-1):
        dis = x[i+1]-x[i]
        if dis<d:
            d = dis
    return d

def minimum_distance(x, y):
    n = len(x)
    
    if n <=1:
        return float('inf')
    if n == 2:
        return math.sqrt((x[0]-x[1])**2+(y[0]-y[1])**2)
    
    m = sum(x)/n
    if x.count(m)==n:
        return minimum_distance_1d(y)
    
    xl = []
    yl = []
    xr = []
    yr = []
    for i in range(n):
        if x[i]<=m:
            xl.append(x[i])
            yl.append(y[i])
        else:
            xr.append(x[i])
            yr.append(y[i])

    dl = minimum_distance(xl, yl)
    dr = minimum_distance(xr, yr)
    d = min(dl,dr)

    xm = []
    ym = []
    for i in range(n):
        if x[i]>m-d and x[i]<m+d:
            xm.append(x[i])
            ym.append(y[i])
            
    xym = list(zip(xm,ym))
    xym_sorted = sorted(xym, key=lambda x:x[1])
            
    np = len(xym_sorted)
    if np > 0:
        for i in range(np-1):
            p = xym_sorted[i]
            for j in range(i+1,min((i+8),np)):
                pj = xym_sorted[j]
                dis = math.sqrt((p[0]-pj[0])**2+(p[1]-pj[1])**2)
                if dis<d:
                    d = dis
    return d
