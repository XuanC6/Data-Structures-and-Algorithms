# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders(object):
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        self.result = []
      
    def inOrder(self,index = 0):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if index == -1:
            return
        self.inOrder(self.left[index])
        self.result.append(self.key[index])
        self.inOrder(self.right[index])
        return self.result

    def preOrder(self,index = 0):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if index == -1:
            return
        self.result.append(self.key[index])
        self.preOrder(self.left[index])
        self.preOrder(self.right[index])
        return self.result


    def postOrder(self,index = 0):
        # Finish the implementation
        # You may need to add a new recursive method to do that
        if index == -1:
            return
        self.postOrder(self.left[index])
        self.postOrder(self.right[index])
        self.result.append(self.key[index])
        return self.result
    
    def reset_result(self):
        self.result = []


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    tree.reset_result()
    print(" ".join(str(x) for x in tree.preOrder()))
    tree.reset_result()
    print(" ".join(str(x) for x in tree.postOrder()))
    tree.reset_result()

threading.Thread(target=main).start()
