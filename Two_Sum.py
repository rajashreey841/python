'''
Problem: Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Author: https://github.com/rajashreey841
'''

import os
import sys

def twosum(nums, target):
    res = []
    for i in range(0,len(nums)):
        leftover = target - nums[i]
        nums[i]="rubbish"
        if (leftover in nums):
            res.append(i)
            res.append(nums.index(leftover))
            return res

if __name__ == "__main__":
    liInt = []
    liStr = input("Enter the list of integers separated by commas:\t")
    target = input("Enter target value:\t")
    li = liStr.split(",")
    for i in li:
        liInt.append(int(i))
    print("Result:",twosum(liInt, int(target)))
