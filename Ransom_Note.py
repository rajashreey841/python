'''
problem:Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

Author:https://github.com/rajashreey841
'''


import os
import sys

def canConstruct(ransomNote, magazine):
        for i in ransomNote:
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True

if __name__ == "__main__":
    i = input("Enter the string :\t")
    j = input("Enter the string :\t")
    print("Result:\t",canConstruct(i,j))
