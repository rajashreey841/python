'''
problem:sum of two numbers in list

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Author:https://github.com/rajashreey841
'''


import os
import sys

def sumNumber(num,k):
    for i in num:
        if k-i in num:
            return True
    return False

if __name__ == "__main__":
    liInt = []
    liStr = input("Enter the list of integers separated by commas:\t")
    target = input("Enter target value:\t")
    li = liStr.split(",")
    for i in li:
        liInt.append(int(i))
    print("Result:",sumNumber(liInt, int(target)))
