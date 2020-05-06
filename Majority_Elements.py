'''
problem:Majority Number

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

Author:https://github.com/rajashreey841
'''


import os
import sys

def majorityElement(nums):
    nums.sort()
    length = len(nums)
    if length%2==0:
        return nums[(length//2)+1]
    else:
        return nums[length//2]
        
if __name__ == "__main__":
    li = []
    i = input("Enter the values separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input values:\t",li)
    print("Result:\t",majorityElement(li))

            