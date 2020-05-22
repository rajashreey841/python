'''
problem:Finding all Anagrams in a string

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input: s: "cbaebabacd" p: "abc"
Output: [0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Author:https://github.com/rajashreey841
'''


import os 
import sys

def findAnagrams(s,p):
        indices = []
        length_p = len(p)
        if length_p > len(s):
            return []
        counter_p = [0] * 26
        for c in p:
            counter_p[ord(c) - 97] += 1
        counter = [0] * 26
        for i in range(length_p - 1):
            counter[ord(s[i]) - 97] += 1
        for i, c in enumerate(s[length_p - 1:]):
            counter[ord(c) - 97] += 1
            if counter_p == counter:
                indices.append(i)
            counter[ord(s[i]) - 97] -= 1
        return indices


if __name__ == "__main__":
    i = input("Enter the string:\t")
    j = input("Enter the string:\t")
    print("Input:\ts=\"",i,"\" p = \"",j,"\"")
    print("Result:",findAnagrams(i,j))
    
        

#print("Input:\tnum = \"",i,"\", k = ",j)

