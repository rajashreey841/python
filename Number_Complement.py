'''
problem:Number Complements
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you to output to 2.

Author:https://github.com/rajashreey841
'''


import os 
import sys

def findComplement(num):
    c = 1
    while num*2 > c:
        num = num^c
        c = c<<1
    return num

if __name__ == "__main__":
    i = int(input("Enter the value\t:"))
    print("Result:\t",findComplement(i))