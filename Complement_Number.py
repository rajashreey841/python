import os 
import sys


def findComplement(num):
    c = 1
    while num*2 > c:
        num = num^c
        c<<1
    return num

if __name__ == "__main__":
    i = int(input("Enter the value\t:"))
    print("Result:\t",findComplement(i))