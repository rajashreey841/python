'''
Problem: Median of Two Sorted Arrays:
----------------------------------------

Given two stored arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be 0(log (m+n)).

Example 1:
Input1 : nums1 = [1,3], nums2 = [2]
output: 2.00000
Explanation : merged array = [1,2,3] and median is 2.

Example 2:
Input2 : nums1 = [1,2], nums2= [3,4]
output:2.50000
Explanation :merged array = [1,2,3,4] and medain is (2+3)/2 =2.5.


Author: https://github.com/rajashreey841
'''

import os
import sys

def findmedian(nums1,nums2):
	res = nums1+nums2
	return float(statistic.median(res))

if __name__ == "__main__":
	nums1 = [1,2]
	nums2 = [3,4]
	print("Result : ",findmedian(nums1,nums2))
