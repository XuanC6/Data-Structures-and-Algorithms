# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 22:31:34 2018

@author: CX
"""
from bst_class import BST

class AVL_BST(BST):
    def AVLInsert(k,R):
        BST.Insert(k)
        N = BST.Find(k)
        AVL_BST.Rebalance(N)
    
    @classmethod
    def Rebalance(cls,N):
        P = N.Parent
        if  N.Left.Height > N.Right.Height+1:
            RebalanceRight(N)
        if N.Right.Height > N.Left.Height+1:
            RebalanceLeft(N)
        AdjustHeight(N)
        if P != null:
            Rebalance(P)
    
    def AdjustHeight(N):
        N.Height = 1+max(N.Left.Height,N.Right.Height)
    
    def RebalanceRight(N):
        M = N.Left
        if M.Right.Height > M.Left.Height:
            RotateLeft(M)
        RotateRight(N)
        AdjustHeight on affected nodes