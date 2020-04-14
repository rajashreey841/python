'''
problem:Longest_common_prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Author: https://github.com/rajashreey841
'''

import os
import sys

def longestCommonPrefix(strs): 
            if not strs:
                return ''
            strs.sort()
            l = min(len(strs[0]), len(strs[-1]))
            i = 0
            while i < l and strs[0][i] == strs[-1][i]:
                    i += 1
            return strs[0][:i]
            
if __name__ == "__main__":
    li=["flower","flow","flight"]
    print(longestCommonPrefix(li))
