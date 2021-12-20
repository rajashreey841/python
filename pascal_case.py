'''
------------------
Program to  Convert Snake case to Pascal case.

Input : geeks_for_geeks
Output : GeeksforGeeks

Author: https://github.com/rajashreey841
'''

import os
import sys
def PascalCase(s):
    return s.replace("_"," ").title().replace(" ","")


if __name__ == "__main__":
    s = input("Enter the string : ")
    print("Output : ",PascalCase(s))
