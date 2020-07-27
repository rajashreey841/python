'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Author:http://github.com/rajashree841
'''

import os
import sys

def containsDuplicate(nums):
    nums.sort()
    if len(nums) != len(set(nums)):
        return True
    else:
        return False

if __name__ == "__main__":
    li = []
    i = input("Enter the value\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input \t",li)
    print("Output \t",containsDuplicate(li))
