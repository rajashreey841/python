'''
problem:Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Author:http://github.com/rajashree841
'''

import os
import sys

def countPrimes(n):
    if n<=2:
        return 0
    is_prime = [ True for _ in range(n) ]   
    is_prime[0] = False
    is_prime[1] = False
    for i in range( 2, int(n ** 0.5)+1 ):
        if not is_prime[i]:
            continue
        for j in range( i*i, n, i):
            is_prime[j] = False
    return sum(is_prime)

if __name__ == "__main__":
    i = int(input("Enter the integer \t"))
    print("Input \t",i)
    print("Output \t",countPrimes(i))