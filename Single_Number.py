'''
problem:Single Number
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Author:https://github.com/rajashreey841
'''

import os 
import sys
def singleNumber(nums):
        for i in nums:
            if(nums.count(i)==1):
                return i

if __name__ == "__main__":
    li = input("Enter the list of integers separated by commas:") 
    l = li.split(",")
    print("Result:",singleNumber(l))
