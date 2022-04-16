'''
problem:Armstrong Number

Example 1:

Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Example 2:

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9

Author:https://github.com/rajashreey841
'''

import sys 
import os

def Armstrongnumber(x):
    n = len(str(x))
    res = x
    sum = 0
    while(res!=0):
        r = res%10
        sum = sum + pow(r,n)
        res = res//10
    return sum == x

if __name__ == "__main__":
    x = int(input("Enter the integer\t"))
    print("Result :",Armstrongnumber(x))   
