'''
problem:Counting Elements 
Given an integer array arr, count element x such that x + 1 is also in arr.
If there're duplicates in arr, count them seperately.

Example 1:
Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.

Author:https://github.com/rajashreey841
'''

import os
import sys
 
def countElements(arr):
        c=0
        for i in arr:
            if i+1 in arr:
                c=c+1
        return c

if __name__ == "__main__":
    li = []
    i = input("Enter the values separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(int(i))
    print("Input : arr = \t",li)
    print("Result\t",countElements(li))