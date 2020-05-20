'''
problem:Remove_duplicate_digits_in_sorted_array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Author:https://github.com/rajashreey841
'''


import os 
import sys

def removeDuplicate(nums):
    count = 0
    while count < len(nums)-1:
        if nums[count] == nums[count+1]:
            nums.pop(count)
        else:
            count+=1
    return nums

if __name__ == "__main__":
    li = []
    i = input("Enter the list of integer separated by comma:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input:",li)
    print("Result:",removeDuplicate(li))
        
                
