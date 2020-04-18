'''
problem:String_Sorting
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Author:https://github.com/rajashreey841
'''

import os
import sys

a = input("enter the string \t")
items=[x for x in a.split(',')]
items.sort()
print (','.join(items))






