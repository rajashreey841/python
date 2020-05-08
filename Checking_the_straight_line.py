'''
problem:Checking the stright line
 You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
Author:https://github.com/rajashreey841
'''


import os
import sys

def checkStraightLine(coordinates):
        if len(coordinates)==2:
            return True
        x0,y0 = coordinates[0]
        x1,y1 = coordinates[1]
        for i in range(2,len(coordinates)):
            x,y = coordinates[i]
            if(y1-y0)*(x-x0)!=(x1-x0)*(y-y0):
                return False
        return True

if __name__ == "__main__":
    Input = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    print("Inputs values:\t",Input)
    print("Result:\t",checkStraightLine(Input))        