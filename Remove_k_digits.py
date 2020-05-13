'''
problem:Remove k Digits
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the th


ree digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Author:https://github.com/rajashreey841
'''


import os
import sys


def removekdigits(num,k):
    stack = []
    a = k
    for i in num:
        while a and stack and stack[-1]>i:
            stack.pop()
            a = a-1
        stack.append(i)
    q = "".join(stack[0:len(num)-k]).lstrip("0")
    if len(q):
        return q
    else:
        return "0"

if __name__ == "__main__":
    i = input("Enter the string:\t")
    j = int(input("Enter the value:\t"))
    print("Input:\tnum = \"",i,"\", k = ",j)
    '''i = "1432219"
    j = 3'''
    print("Result:\t\"",removekdigits(i,j),"\"")