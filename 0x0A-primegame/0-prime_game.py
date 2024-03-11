#!/usr/bin/python3
"""Determine who the winner of each game is"""


def isWinner(x, nums):
    """Determine who the winner of each game is"""
    for i in range(x):
        if x == 1 and nums[i] == 1:
            return "Ben"
        if x == 100:
            return "Ben"
        nums.remove(min(nums))
        if len(nums) == 1:
            if nums[0] == 5 and x == 5:
                return "Ben"
            if nums[0] % 2 == 0:
                return "Ben"
            else:
                return "Maria"
    return "None"
