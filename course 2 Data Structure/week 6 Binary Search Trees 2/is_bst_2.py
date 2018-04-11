#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**32)  # new thread will get stack of such size

def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
        
    def LeftDescendant(index):
        now = tree[index]
        if now[1] == -1:
            return now
        else:
            return LeftDescendant(now[1])
    def RightDescendant(index):
        now = tree[index]
        if now[2] == -1:
            return now
        else:
            return RightDescendant(now[2])

    def TwoNeighbor(index = 0):
        if len(tree) == 0:
            return True
        if index == -1:
            return True
        now = tree[index]
        if now[2]!=-1:
            now_next = LeftDescendant(now[2])
            if now_next[0]<=now[0]:
                return False
        if now[1]!=-1:
            now_prev = RightDescendant(now[1])
            if now_prev[0]>=now[0]:
                return False
        return (TwoNeighbor(now[2]) and TwoNeighbor(now[1]))

    if TwoNeighbor():
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()