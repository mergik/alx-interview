#!/usr/bin/python3
"""
this module contains
a method that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    keys = set()
    for i in range(len(boxes)):
        if i not in keys and i != 0:
            return False
        for elem in boxes[i]:
            if elem < len(boxes):
                keys.update(boxes[elem])
        keys.update(boxes[i])
    return True
