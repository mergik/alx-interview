#!/usr/bin/python3
""" fewest number of operations"""


def minOperations(n):
    """
    method calculates the fewest number of operations needed
    """
    copy = 1
    paste = 0
    count = 0
    if copy > n:
        return 0
    while copy < n:
        if n % copy == 0 and copy > paste:
            paste = copy
        else:
            copy += paste
        count += 1
    return count
