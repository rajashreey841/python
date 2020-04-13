'''
problem:Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Author: https://github.com/rajashreey841
'''

import os
import sys

def isPalindrome(x):
    temp = x
    rev = 0
    while(x > 0):
        rev = rev*10
        rev += x % 10
        x = x//10
    if(temp == rev):
        return True
    else:
        return False

if __name__ == "__main__":
    print(isPalindrome(121))



