''''
problem:Contiguous Array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Author:https://github.com/rajashreey841
'''


import os
import sys

def findMaxLength(nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        presum = 0
        res = 0
        dic = {presum:-1} 
        for i, num in enumerate(nums):
            presum += num
            if presum in dic:
                res = max(res, i - dic[presum])
            else:
                dic[presum] = i
        return res

if __name__ == "__main__":
    li = []
    i = input("Enter the values separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input List:\t", li)
    print("Result",findMaxLength(li))

    