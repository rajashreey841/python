'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:
Input: "Hello World"
Output: 5

Author:https://github.com/rajashreey841
'''

import os
import sys

def lenghtOfLastWord(s):
    r = s.split()
    if len(r) >= 1:
        return len(r[-1])
    else:
        return 0

if __name__ == "__main__":
    i = input("Enter the string \t")
    print("Input:\t \"",i ,"\"")
    print("Output\t",lenghtOfLastWord(i))