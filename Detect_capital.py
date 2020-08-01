'''
problem:Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:
Input: "USA"
Output: True
 
Example 2:
Input: "FlaG"
Output: False

Author:http://github.com/rajashreey841
'''

import os
import sys

def detect_capital(word):
	if word.upper() == word:
			return True
	elif word[:0].isupper() and word[:1].islower():
		return True
	elif word.lower() == word:
		return True
	return False


if __name__ == "__main__":
		i = input("Enter the String\t")
		print("Input: \t\"",i,"\"")
		print("Output \t",detect_capital(i))


















