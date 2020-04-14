'''
problem:Valid_Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 3:
Input: "(]"
Output: false

Author:https://github.com/rajashreey841
'''

import os
import sys
 
def isValid(s):
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            else:
                if stack and c==stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack

if __name__ == "__main__":
    input="()"
    print(isValid(input))