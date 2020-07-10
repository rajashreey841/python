'''
problem:Mininum cost of climbing stair
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Author:https://github.com/rajashreey841
'''

import os 
import sys

def minCostClimbingStairs(cost):
    stairs = {}
    stairs[0] = cost[0]
    stairs[1] = cost[1]
    for i in range(2,len(cost)):
        stairs[i] = cost[i]+min(stairs[i-1],stairs[i-2])
    return min(stairs[len(cost)-1],stairs[len(cost)-2])

if __name__ == "__main__":
    li = []
    i = input("Enter the interger to separate from comma\t")
    listr = i.split(",")
    for i in listr:
        li.append(int(i))
    print("Input \t",li)
    print("Output\t",minCostClimbingStairs(li))