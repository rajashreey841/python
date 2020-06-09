'''
problem:Reverse String ll

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Author: https://github.com/rajashreey841
'''


import os
import sys

def reverseStringll(s):
    vowels = set("AaEeIiOoUu")
    i,j = 0,len(s)-1
    s = list(s)
    while(i<j):
        if s[i] not in vowels:
            i+=1
        elif s[j] not in vowels:
            j-=1
        if s[i] in vowels and s[j] in vowels:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
    return "".join(s)

if __name__ == "__main__":
    i = input("Enter the strig \t")
    print("Input:\"",i,"\"")
    print("output:\"",reverseStringll(i),"\"")

        
        