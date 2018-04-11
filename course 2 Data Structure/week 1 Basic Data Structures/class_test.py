# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 20:37:15 2018

@author: CX
"""
import random

def fib_gen(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b


class Test(object):
    def __init__(self):
        self.val = random.randint(1,10)
    
#    @classmethod
#    def recur(cls,n):
#        if n == 0:
#            return 0
#        if n == 1:
#            return 1
#        else:
#            return (cls.recur(n-1)+cls.recur(n-2))

    def recur(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return (self.recur(n-1)+self.recur(n-2))

    def call_recur(self):
        print(self.val)
        print(self.recur(self.val))
        
        
        
it = fib_gen(10)
for num in it:
    print(num)
print('\n')

lis = Test()
lis.call_recur()

#print('\n')

#print(Test.recur(9))