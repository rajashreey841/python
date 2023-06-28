'''
problem:Add Binary

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Author:https://github.com/rajashreey841
'''


import os
import sys

def addBinary(a,b):
     return str(bin(int(a,2)+int(b,2)))[2:]

if __name__ == "__main__":
    i = input("Enter the string\t")
    j = input("Enter the string\t")
    print("Input:\ta =\"",i ,"\"","b =\"",j,"\"")
    print("Result:",addBinary(i,j))
q

