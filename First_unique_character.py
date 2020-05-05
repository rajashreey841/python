'''
problem:First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Author:https://github.com/rajashreey841
'''


import os
import sys


def firstUniqChar(s):
    for i,j in enumerate(s):
        if(s.count(j)==1):
            return i
    return -1  
		
if __name__ == "__main__":
    i = input("Enter the string:\t")
    print("Result:\t",firstUniqChar(i))
