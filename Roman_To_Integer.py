'''
problem:Roman to Integer

Roman number are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: "III"
Output: 3

Example 2:
Input: "IV"
Output: 4

Author: https://github.com/rajashreey841
'''

import os
import sys

def romanToInt(s):
    romanDict={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    sum = 0
    f = 0
    for i in range(0,len(s)):
        if (f == 1):
            f = 0
            continue
        elif(i < (len(s)-1)):
            if ((s[i]=="I") and (s[i+1]=="V")):
                sum = sum + 4
                f = 1
            elif ((s[i]=="I") and (s[i+1]=="X")):
                sum = sum + 9
                f = 1
            elif ((s[i]=="X") and (s[i+1]=="L")):
                sum = sum + 40
                f = 1
            elif ((s[i]=="X") and (s[i+1]=="C")):
                sum = sum + 90
                f = 1
            elif ((s[i]=="C") and (s[i+1]=="D")):
                sum = sum + 400
                f = 1
            elif ((s[i]=="C") and (s[i+1]=="M")):
                sum = sum + 900
                f = 1
            else:
                sum = sum + romanDict[s[i]]
        else:
            sum = sum + romanDict[s[i]]
    return sum

if __name__ == "__main__":
    print("Result = ", romanToInt("III"))
