# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:30:05 2019

@author: Edu
"""

class ParentA:
    def explore(self):
        print("explore() method called")
 
class ParentB:
    def search(self):
        print("search() method called")
 
class ParentC:
    def discover(self):
        print("discover() method called")
 
class D(ParentA, ParentB, ParentC):
    def test(self):
        print("test() method called")
 
 
d_obj = D()
d_obj.explore()
d_obj.search()
d_obj.discover()
d_obj.test()
