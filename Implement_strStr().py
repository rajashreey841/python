'''
problem: Implements strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Author:https://github.com/rajashreey841
'''


import os 
import sys

def strStr(haystack,needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

if __name__ == "__main__":
    i = input("Enter the string:\t")
    j = input("Enter the string:\t")
    print("Input: haystack= ",i ," needle =" ,j )
    print("output:",strStr(i,j))
