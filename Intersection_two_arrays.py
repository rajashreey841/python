'''
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Author:https://github.com/rajashreey841
'''

import os
import sys

def intersectionTwoArrays(nums1,nums2):
    return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    li = []
    li1 = []
    n1 = input("Enter the integer\t")
    n2 = input("Enter the Integer\t")
    liStr1 = n1.split(",")
    liStr2 = n2.split(",")
    for n1 in liStr1:
        li.append(int(n1))
    for n2 in liStr2:
        li1.append(int(n2))
    print("Input:\t nums1 =",li,", nums2 =",li1)
    print("output:\t",intersectionTwoArrays(li,li1))