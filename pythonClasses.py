# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 23:01:30 2019

@author: Edu
"""

class car:
     
     def __init__(self,speed,color):
        print(speed,color)
        self.speed = speed
        self.__color = color # the double underscore is the python convention
        # to makean atributte private
        print('the __init__ is called')
        
     def printer(self):
         print('Velocidad: {} , color: {}'.format(self.speed,self.__color))
        
ford = car(100,'blue')
honga = car(130,'red')

ford.speed = 10000

ford.printer()
honga.printer()

print(ford.__color)