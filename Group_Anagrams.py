'''
problem:Group Anagrams
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Author:https://github.com/rajashreey841
'''


import os
import sys

def groupAnagrams(strs):
        res = []
        d = {("".join(sorted(i))):[] for i in strs}
        for i in strs:
            d["".join(sorted(i))].append(i)
        for k in d:
            res.append(d[k])
        return res

if __name__ == "__main__":
    li = []
    i = input("Enter the string separated by commas:\t")
    liStr = i.split(",")
    for i in liStr:
        li.append(str(i))
    print("Input :\t",li)
    print("Result:\t",groupAnagrams(li))