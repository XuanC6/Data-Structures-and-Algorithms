#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**32)  # new thread will get stack of such size

class OrderTree(object):
    def __init__(self,tree,result = []):
        self.tree = tree
        self.result = result
    
    def inOrder(self,index = 0):
        if len(self.tree) == 0:
            return
        if index == -1:
            return
        now = self.tree[index]
        self.inOrder(now[1])
        self.result.append(now[0])
        self.inOrder(now[2])

def IsBinarySearchTree(result):
    # Implement correct algorithm here
    if len(result) == 0:
        return True
    for i in range(len(result)-1):
        if result[i]>=result[i+1]:
            return False
    return True

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    the_order = OrderTree(tree)
    the_order.inOrder()
    if IsBinarySearchTree(the_order.result):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
