# -*- coding: utf-8 -*-
"""
Spyder Editor

Binary Search Tree Psudocode
"""
'''
Basic Operations of A Binary Search Tree
'''
'''
Find
'''
def Find(k,R):
    if R.Key == k:
        return R
    elif R.Key > k :
        if R.Left != null:
            return Find(k,R.Left)
        return R
    elif R.Key < k :
        if R.Right != null:
            return Find(k,R.Right)
        return R
'''
Next
'''
def Next(N):
    if N.Right != null:
        return LeftDescendant(N.Right)
    else:
        return RightAncestor(N)

def LeftDescendant(N):
    if N.Left == null:
        return N
    else:
        return LeftDescendant(N.Left)

def RightAncestor(N):
    if N.Parent.Key != null:
        if N.Key < N.Parent.Key:
            return N.Parent
        else:
            return RightAncestor(N.Parent)
    return null
'''
Search
'''
def RangeSearch(x,y,R):
    L = []
    N = Find(x,R)
    while N.Key <= y:
        if N.Key >= x:
            L.Append(N)
        N = Next(N)
    return L
'''
Insert
'''
def Insert(k,R):
    P = Find(k,R)
    if k<P.Key:
        Add new node with key k as a left child of P
    elif k>P.Key:
        Add new node with key k as a right child of P
'''
Delete
'''
def Delete(N):
    if N.Right == null:
        P = N.Parent
        L = N.Left
        if P != null and L!=null:
            L.Parent = P
            if L.Key<P.Key:
                P.Left = L
            else:
                P.Right = L
        if P == null and L!=null:
            L.Parent = null
        if P!=null and L==null:
            if N.key > P.key:
                P.Right = null
            else:
                P.Left = null
        del(N)
    else:
        X = Next(N)
    '''
    Note that X.Left = null
    '''
        N.Key = X.Key

        R = X.Right
        PX = X.Parent
        
        R.Parent = PX
        if R.Key < PX.key:
            PX.Left = R
        else:
            PX.Right = R
        
        del(X)
        
'''
Rotate
'''
def RotateRight(X):
    '''
    Y is X's left child, after rotation,X is Y's right child
    '''
    P = X.Parent
    Y = X.Left
    B = Y.Right
    Y.Parent = P
    if Y.Key<P.Key:
        P.Left = Y
    else:
        P.Right = Y
    X.Parent = Y
    Y.Right = X
    B.Parent = X
    X.Left = B

def RotateLeft(X):
    '''
    Y is X's right child, after rotation,X is Y's left child
    '''
    P = X.Parent
    Y = X.Right
    B = Y.Left
    Y.Parent = P
    if Y.Key<P.Key:
        P.Left = Y
    else:
        P.Right = Y
    X.Parent = Y
    Y.Left = X
    B.Parent = X
    X.Right = B
    
    
'''
AVL Tree
AVL property
For all nodes N:
    |N.Left.Height-N.Right.Height|<=1
'''
'''
Let N be a node of a binary tree satisfying
the AVL property. Let h = N.Height. Then
the subtree of N has size at least the
Fibonacci Number F_h .
'''

'''
AVL tree Insert

Heights stay the same except on the insertion path(path to search it)
'''

def AVLInsert(k,R):
    Insert(k,R)
    N = Find(k,R)
    Rebalance(N)
    
def Rebalance(N):
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

'''
AVL tree Delete
'''
def AVLDelete(N):
    Delete(N)
    M = Parent of node replacing N
    Rebalance(M)

'''
Merge
'''
def MergeWithRoot(R_1 ,R_2 ,T):
    T.Left = R_1
    T.Right = R_2
    R_1.Parent = T
    R_2.Parent = T
    return T
    '''
    Time = O(1)
    '''

def Merge(R_1 ,R_2):
    T = Find(float('inf'),R_1)
    R_1.Delete(T)
    MergeWithRoot(R_1 ,R_2,T)
    return T
    '''
    Time = O(h)
    '''

def AVLTreeMergeWithRoot(R_1 ,R_2 ,T):
    if abs(R_1.Height - R_2.Height) <= 1:
        MergeWithRoot(R_1 ,R_2 ,T)
        T.Height = max(R_1.Height,R_2.Height) + 1
        return T
    else if R_1.Height > R_2.Height:
        R_Prime = AVLTreeMergeWithRoot(R_1.Right,R_2,T)
        R_1.Right = R_Prime
        R_Prime.Parent = R_1
        Rebalance(R_1)
        return T
    else if R_1.Height < R_2.Height:
        R_Prime = AVLTreeMergeWithRoot(R_1,R_2.Left,T)
        R_2.Left = R_Prime
        R_Prime.Parent = R_2
        Rebalance(R_2)
        return T
    '''
    Time=O(|R_1.Height − R_2.Height| + 1)
    '''
    
'''
Split
'''
def Split(R,x):
    if R = null:
        return (null,null)
    if x ≤ R.Key:
        (R_1 ,R_2) = Split(R.Left,x)
        R_3 = MergeWithRoot(R_2 ,R.Right,R)
        return (R_1 ,R_3)
    if x > R.Key:
        (R_1 ,R_2) = Split(R.Right,x)
        R_3 = MergeWithRoot(R.Left,R_1,R)
        return (R_3 ,R_2)
    
    
    
    
    
    
    
    