'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Author:http://github.com/rajashree841
'''

import os
import sys

def mergeSortedArray( m, n, num1, num2):
    j = 0
    for i in range(m,m + n):
        num1[i] = num2[j]
        j+=1
    num1.sort()
    return num1

if __name__ == "__main__":
    a = int(input("Enter the value\t"))
    b = int(input("Enter the value\t"))
    lin1 = []
    lin2 = []
    liStrn1 = (input("Enter the values separated by commas:\t")).split(",")
    liStrn2 = (input("Enter the values separated by commas:\t")).split(",")
    for n1 in liStrn1:
        lin1.append(int(n1))
    for n2 in liStrn2:
        lin2.append(int(n2))
    print("Output\t",mergeSortedArray(a,b,lin1,lin2))
