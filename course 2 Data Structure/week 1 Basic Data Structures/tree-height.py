# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node(object):
    
    def __init__(self,parent_index = -1,children_index_list=[]):
        self.parent_index = parent_index
        self.children_index_list = children_index_list
    
    def add_child(self,new_child_index):
        self.children_index_list.append(new_child_index)
    
    def set_parent(self,new_parent_index):
        self.parent_index = new_parent_index


class TreeHeight:
    
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        
        
    def construct_tree(self):
        self.nodes = [Node(-1,[]) for i in range(self.n)]
        
        for i in range(self.n):
            parent_index = self.parent[i]
            self.nodes[i].set_parent(parent_index)
            if parent_index != -1:
                self.nodes[parent_index].add_child(i)
    


    def compute_height(self):
        
        heights = [-1]*self.n
        nodes = self.nodes
        
        def node_height(nodes,heights,i):
        
            node = nodes[i]
            parent_index = node.parent_index
            if parent_index == -1:
                return 1
            else:
                if heights[parent_index]!=-1:
                    return heights[parent_index]+1
                else:
                    return node_height(nodes,heights,parent_index)+1

        
        for i in range(self.n):
            heights[i] = node_height(nodes,heights,i)
        return max(heights)



def main():
    tree = TreeHeight()
    tree.read()
    tree.construct_tree()
    print(tree.compute_height())

threading.Thread(target=main).start()
