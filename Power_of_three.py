'''
problem:Power of Three
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Author:http://github.com/rajashreey841
'''

import os
import sys

def powerOfThree(n):
    while(n % 3 ==0 and n != 0):
        n /= 3
    if n == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    i = int(input("Enter the integer\t"))
    print("Input:\t",i)
    print("Output:\t",powerOfThree(i))


