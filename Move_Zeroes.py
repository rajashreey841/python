'''
problem:Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Author:https://github.com/rajashreey841
'''
  
import os
import sys

def moveZeroes(nums):

    for i in nums:
        if i==0:
            nums.append(nums.pop(nums.index(i)))
    return nums

if __name__ == "__main__":
    li = []
    i = input("Enter the values separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input values:\t",li)
    print("Result:\t",moveZeroes(li))