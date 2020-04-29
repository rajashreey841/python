'''
problem:Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Author:https://github.com/rajashreey841
'''

import os
import sys

def maxSubArray(nums):
        curSum = nums[0]
        maxSum = nums[0]
        
        for i in nums[1:]:
            curSum = max(i, curSum + i)
            maxSum = max(curSum, maxSum)
            
        return maxSum

if __name__ == "__main__":
    li = []
    i = input("Enter the values separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input List:\t", li)
    print("Result",maxSubArray(li))

    