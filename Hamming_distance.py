
'''
problem:Hamming distance

Example 1:
Input1: n1 = 9, n2 = 14
Output: 3
9 = 1001, 14 = 1110
No. of Different bits = 3

Input2: n1 = 4, n2 = 8
Output: 2 

Author:https://github.com/rajashreey841
'''

import os
import sys

def Hammingdistance(n1,n2):
    r = n1 ^ n2
    res = 0
    while(r>0):
        res+= r&1
        r>>=1
    return res

if __name__ == "__main__":
    i = int(input("Enter the integer"))
    j = int(input("Enter the integer"))
    print("Result :",Hammingdistance(i,j))

