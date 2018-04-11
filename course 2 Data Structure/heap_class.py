# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 17:41:54 2018

@author: CX
"""

class HeapMin(object):
    def __init__(self):
        self.data = []
    
    def ReadData(self):
        self.n = int(input())
        self.data = [int(s) for s in input().split()]
        assert self.n == len(self.data)
    
    def ShiftUp(self,i):
#        while i>0 and lines[parent_index(i)][1]<lines[i][1]:
#            ori_par_i = lines[parent_index(i)][0]
#            ori_i = lines[i][0]
#            lines[i],lines[parent_index(i)] = lines[parent_index(i)],lines[i]
#            lines_index[ori_i],lines_index[ori_par_i] = lines_index[ori_par_i],lines_index[ori_i]
#            i = parent_index(i)

    def ShiftDown(self,i):
        min_index = i
        
        left_child_i = 2*i+1
        if left_child_i<self.n and self.data[left_child_i]<self.data[min_index]:
            min_index = left_child_i
        
        right_child_i = 2*i+2
        if right_child_i<self.n and self.data[right_child_i]<self.data[min_index]:
            min_index = right_child_i
        
        if i != min_index:
            self.data[i],self.data[min_index] = self.data[min_index],self.data[i]
            self.ShiftDown(min_index)
    
    def GenerateSwaps(self):
        for i in range(((self.n-1)//2)+1):
            j = (self.n-1)//2 -i
            self.ShiftDown(j)
    
    def Extract(self):

