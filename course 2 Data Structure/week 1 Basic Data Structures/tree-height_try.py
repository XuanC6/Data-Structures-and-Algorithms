# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 21:07:10 2018

@author: CX
"""

class Node(object):
    
    def __init__(self,parent_index = -1,children_index_list=[]):
        self.parent_index = parent_index
        self.children_index_list = children_index_list
    
    def add_child(self,new_child_index):
        self.children_index_list.append(new_child_index)
    
    def set_parent(self,new_parent_index):
        self.parent_index = new_parent_index


class TreeHeight(object):
    
    def __init__(self,parent_list):
        self.n = len(parent_list)
        self.parent = parent_list
        self.nodes = [Node(-1,[]) for i in range(self.n)]

        
    def construct_tree(self):

        for i in range(self.n):
            parent_index = self.parent[i]
            self.nodes[i].set_parent(parent_index)
            if parent_index != -1:
                self.nodes[parent_index].add_child(i)
    
#    def compute_height(self):
#
#        heights = [float('-inf')]
#        for node in self.nodes:
#            if node.children_index_list == []:
#                new_height = 1
#                while node.parent_index != -1:
#                    node = self.nodes[node.parent_index]
#                    new_height += 1
#                heights.append(new_height)
#
#        return max(heights);

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



parent_list = [-1,0,4,0,3]
tree = TreeHeight(parent_list)
tree.construct_tree()
nodes = tree.nodes
for node in nodes:
    print(node.parent_index)
    print(node.children_index_list)
print(tree.compute_height())





