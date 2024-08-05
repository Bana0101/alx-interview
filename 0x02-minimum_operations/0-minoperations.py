#!/usr/bin/python3
"""
A function that calculates the minimum operations to copy and paste letters
"""


def minOperations(n):
    oper = 0
    min = 2
    while n > 1:
        while n % min == 0:
            oper += min
            n /= min
        min += 1
    return oper
