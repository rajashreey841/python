'''
problem:Single Element in sorted array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Author:https://github.com/rajashreey841
'''


import os
import sys

def singleNonDuplicate(nums):
        left = 0
        right = len(nums)-1
        while(left<right):
            mid = (left+right)//2
            check_even = (right-mid)%2==0
            if nums[mid+1]== nums[mid]:
                if check_even:
                    left = mid+2
                else:
                    right = mid-1
            elif nums[mid-1]==nums[mid]:
                if check_even:
                    right = mid-2
                else:
                    left = mid+1
            else:
                return nums[mid]
        return nums[left]
        
if __name__ == "__main__":
    li = []
    i = input("Enter the values separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input values:\t",li)
    print("Result:\t",singleNonDuplicate(li))  