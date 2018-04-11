#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**32)  # new thread will get stack of such size

def IsBinarySearchTree(result):
    if len(result) == 0:
        return True
    for i in range(len(result)-1):
        if result[i][0]>result[i+1][0]:
            return False
        if result[i][0]==result[i+1][0]:
            if result[i][1]>result[i+1][1]:
                return False
    return True

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    result = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
        
#    def treeProcess(index = 0,i = 0):
#        if len(tree) == 0:
#            return
#        if index == -1:
#            return
#        now = tree[index]
#        tree[index][0] = (now[0],i)
#        treeProcess(now[1],2*i+1)
#        treeProcess(now[2],2*i+2)
#        
#    treeProcess()
    
    def inOrder(index = 0,i = 0):
        if len(tree) == 0:
            return
        if index == -1:
            return
        now = tree[index]
        inOrder(now[1],2*i+1)
        result.append((now[0],i))
        inOrder(now[2],2*i+2)
        
    inOrder()

    if IsBinarySearchTree(result):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
