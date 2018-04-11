# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:43:54 2018

@author: CX
"""

# python3

#import sys

n, m = 6,4
lines = [10,0,5,0,3,3]
lines = [[i,lines[i]] for i in range(n)]
lines_index = list(range(n))
rank = [1] * n
parent = list(range(n))

def parent_index(i):
    return max((i-1)//2,0)

def shift_up(i):
    global lines,lines_index

    while i>0 and lines[parent_index(i)][1]<lines[i][1]:
        ori_par_i = lines[parent_index(i)][0]
        ori_i = lines[i][0]
        lines[i],lines[parent_index(i)] = lines[parent_index(i)],lines[i]
        lines_index[ori_i],lines_index[ori_par_i] = lines_index[ori_par_i],lines_index[ori_i]
        i = parent_index(i)

def shift_down(i):
    global lines,n
    max_index = i
    
    left_child_i = 2*i+1
    if left_child_i<n and lines[left_child_i][1]>lines[max_index][1]:
        max_index = left_child_i
    
    right_child_i = 2*i+2
    if right_child_i<n and lines[right_child_i][1]>lines[max_index][1]:
        max_index = right_child_i
    
    if i != max_index:
        ori_max_i = lines[max_index][0]
        ori_i = lines[i][0]
        lines[i],lines[max_index] = lines[max_index],lines[i]
        lines_index[ori_i],lines_index[ori_max_i] = lines_index[ori_max_i],lines_index[ori_i]
        shift_down(max_index)

def build_heap():
    global n
    for i in range(((n-1)//2)+1):
        j = (n-1)//2 -i
        shift_down(j)

def getParent(table):
    global parent
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]

def merge(destination, source):
    global rank,lines,ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return
    rD_i = lines_index[realDestination]
    rS_i = lines_index[realSource]

    if rank[realDestination]>=rank[realSource]:
        parent[realSource] = realDestination
        lines[rD_i][1] += lines[rS_i][1]
        shift_up(rD_i)
        if rank[realDestination]==rank[realSource]:
            rank[realDestination]+=1
    if rank[realDestination]<rank[realSource]:
        parent[realDestination] = realSource
        lines[rS_i][1] += lines[rD_i][1]
        shift_up(rS_i)
        
    ans = lines[0][1]

build_heap()
print(lines)
#for i in range(m):
#    destination, source = map(int, sys.stdin.readline().split())
#    merge(destination - 1, source - 1)
#    print(ans)
    
