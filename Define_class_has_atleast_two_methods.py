
'''
problem:Defining class with two methods
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
Author:https://github.com/rajashreey841
'''

import os
import sys


class Two_method():
    def __int__(self):
        self.s=""
    def getstring(self):
        self.s=input("enter the values")
    def putstring(self):
         print(self.s.upper())
a=Two_method()
a.getstring()
a.putstring()