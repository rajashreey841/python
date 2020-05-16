'''
problem: Maximum Sum Circular Subarry

Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.
Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.
Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

Example 1:
Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3

Example 2:
Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10

Author:https://github.com/rajashreey841
'''


import os 
import sys

def maxSubarraySumCircular(A):
    
    min_sum = A[0]
    max_sum = A[0]
    sub_min = A[0]
    sub_max = A[0]
    total_sum = A[0]

    for num in A[1:]:
         
        total_sum+=num
        sub_max = max(num,sub_max+num)
        sub_min = min(num,sub_min+num)

        max_sum = max(max_sum,sub_max)
        min_sum = min(min_sum,sub_min)

    if total_sum-min_sum>max_sum>0:
        return total_sum-min_sum
    else:
        return max_sum

if __name__ == "__main__":
    li = []
    i = input("Enter the value separted by comma:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input value :\t",li)
    print("Output:\t",maxSubarraySumCircular(li))