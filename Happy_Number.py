'''
problem:Happy Number

Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
Return True if n is a happy number, and False if not.

Example: 
Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Author:https://github.com/rajashreey841
'''

import os 
import sys

def isHappy(n):
        c=0
        if n==1:
            return True
        while n!=1 and c<30:
            c=c+1
            sum=0
            for i in str(n):
                sum+=int(i)*int(i)
            n=sum
            if n==1:
                return True
        return False
        
if __name__ == "__main__":
    i = input("Enter the value\t")
    print("Result",isHappy(i))        