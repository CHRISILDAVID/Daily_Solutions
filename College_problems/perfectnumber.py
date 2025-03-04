"""
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding
the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false
"""
def isperfect(n):
    s = 0
    i = 1
    while i <= n//2: # iterates from 1 to n//2
        if n%i == 0: # check for factors of n
            s += i
        i += 1
    if s == n:
        return True
    else:
        return False

print(isperfect(7))