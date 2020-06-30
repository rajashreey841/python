'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Author: https://github.com/rajashreey841
'''


import os
import sys

def searchInsert(nums,target):
    if target in nums:
            return nums.index(target)
    for i in nums:
        if i>target:
            return nums.index(i)
    return len(nums)
if __name__ == "__main__":
    liInt = []
    liStr = input("Enter the list of integers separated by commas:\t")
    target = input("Enter target value:\t")
    li = liStr.split(",")
    for i in li:
        liInt.append(int(i))
    print("Result:",searchInsert(liInt, int(target)))
