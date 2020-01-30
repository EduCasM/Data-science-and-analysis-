# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:47:30 2019

@author: Edu
"""
class A:
    def explore(self):
        print("explore() method from class A")
 
class B(A):
    def explore(self):
        print("explore() method from class B")
 
 
b_obj = B()
a_obj = A()
 
b_obj.explore()
a_obj.explore()

class C:
    def explore(self):
        print("explore() method from class C")
 
class D(C):
    def explore(self):
        super().explore()  # calling the parent class explore() method
        print("explore() method from class D")
 
 
d_obj = D()
d_obj.explore()