'''
problem:math operation

Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program .

Example
100
The output of the program should be:
18

Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26)
In case of input data being supplied to the question, it should be assumed to be a console input. 

Author:https://github.com/rajashreey841
'''

import os
import sys
import math

c = 50    
h = 30
d = input("Enter the values:\t")
prod = 2*c*d
div = prod // h
print("Result:\t", math.floor(math.sqrt(div)))

