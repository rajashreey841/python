'''
problem:Factorial problem

Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.

Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Author:https://github.com/rajashreey841
'''

import os
import sys
  

def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)

if __name__ == "__main__":
    print(fact(8))