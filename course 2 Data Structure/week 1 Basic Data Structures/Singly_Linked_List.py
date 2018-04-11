# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:24:31 2018

@author: CX
"""
class Node(object):
    
    def __init__(self,key,next_node=None):
        self.key = key
        self.next_node = next_node
    
    def set_next_node(self,next_node):
        self.next_node = next_node
    
    def  __del__(self):
        pass

class Singly_Linked_List(object):
    
    def __init__(self,head=None,tail=None,lengh = 0):
        self.head = head
        self.tail = tail
        self.length = lengh
    
    def popfront(self):
        if self.length > 0:
            front_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = front_node.next_node
            self.length -= 1
            del(front_node)
    
    def pushback(self,key):
        new_last_node = Node(key)
        
        if self.length == 0:
            self.tail = new_last_node
            self.head = self.tail
        else:
            self.tail.set_next_node(new_last_node)
            self.tail = new_last_node
        self.length += 1

