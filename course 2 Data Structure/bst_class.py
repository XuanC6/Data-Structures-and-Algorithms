# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 20:18:45 2018

@author: CX
"""
class Node(object):
    def __init__(self,Key,Parent = None,Left = None,Right = None,Height = 1,Size = 1):
        self.Key = Key
        self.Parent = Parent
        self.Left = Left
        self.Right = Right
        self.Height = Height
        self.Size = Size


class BST(object):
    def __init__(self):
        self.Root = None
    
    def Insert(self,k):
        if self.Root == None:
            self.Root = Node(k)
            return
        P = self.FindKey(k)
        if P.Key == k:
            return
        if k < P.Key:
            P.Left = Node(k)
            P.Left.Parent = P
        elif k > P.Key:
            P.Right = Node(k)
            P.Right.Parent = P
        BST.UpdateSize(P)
        BST.UpdateHeight(P)

    def Delete(self,N):
        if N == None:
            return
        if N.Right == None:
            P = N.Parent
            L = N.Left
            if P != None and L != None:
                L.Parent = P
                if L.Key < P.Key:
                    P.Left = L
                else:
                    P.Right = L
            if P == None and L != None:
                L.Parent = None
                self.Root = L
            if P != None and L == None:
                if N.Key > P.Key:
                    P.Right = None
                else:
                    P.Left = None
            if P == None and L == None:
                self.Root = None
            del(N)
            BST.UpdateSize(P)
            BST.UpdateHeight(P)
        else:
            X = BST.Next(N)
            #Note that X.Left = null
            KeyX = X.Key
            PX = X.Parent
            RX = X.Right
            if RX == None:
                if KeyX < PX.Key:
                    PX.Left = None
                else:
                    PX.Right = None
            else:
                RX.Parent = PX
                if RX.Key < PX.Key:
                    PX.Left = RX
                else:
                    PX.Right = RX
            del(X)
            N.Key = KeyX
            BST.UpdateSize(PX)
            BST.UpdateHeight(PX)
            
    def FindKey(self,k):
        return BST.Find(k,self.Root)

    def RangeSearch(self,x,y):
        L = []
        N = self.FindKey(x)
        while N.Key <= y:
            if N.Key >= x:
                L.append(N)
            N = BST.Next(N)
        return L

    @classmethod
    def Find(cls,k,R):
        if R.Key == k:
            return R
        elif R.Key > k :
            if R.Left != None:
                return BST.Find(k,R.Left)
            return R
        elif R.Key < k :
            if R.Right != None:
                return BST.Find(k,R.Right)
            return R

    @classmethod
    def Next(cls,N):
        if N.Right != None:
            return BST.LeftDescendant(N.Right)
        else:
            return BST.RightAncestor(N)
        
    @classmethod
    def LeftDescendant(cls,N):
        if N.Left == None:
            return N
        else:
            return BST.LeftDescendant(N.Left)
    
    @classmethod
    def RightAncestor(cls,N):
        if N.Parent.Key != None:
            if N.Key < N.Parent.Key:
                return N.Parent
            else:
                return BST.RightAncestor(N.Parent)
        return None
    
    @classmethod
    def UpdateSize(cls,N):
        while N != None:
            N.Size = 1
            if N.Left != None:
                N.Size += N.Left.Size
            if N.Right != None:
                N.Size += N.Right.Size
            N = N.Parent
            
    @classmethod
    def UpdateHeight(cls,N):
        while N != None:
            N.Height = 1
            heights = []
            if N.Left != None:
                heights.append(N.Left.Height)
            if N.Right != None:
                heights.append(N.Right.Height)
            if heights != []:
                N.Height += max(heights)
            N = N.Parent

