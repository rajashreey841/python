'''
problem:Power of Two
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false

Author:http://github.com/rajashreey841
'''

import os
import sys

def powerOfTwo(n):
    i = 0
    r = 1
    while r < n:
        i = i+1
        r = 2**i
    if r == n:
        return True
    else:
        return False

if __name__ == "__main__":
    i = int(input("Enter the integer\t"))
    print("Input:\t",i)
    print("Output:\t",powerOfTwo(i))

