'''
problem:Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.

Author:http//github.com/rajashreey841
'''

import os 
import sys

def addDigits(num):
    if num < 10:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

if __name__ == "__main__":
    i = int(input("Enter the integer\t"))
    print("Input \t",i)
    print("Output \t",addDigits(i))
    