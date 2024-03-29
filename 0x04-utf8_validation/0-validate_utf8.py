#!/usr/bin/python3
"""determines if given data set reps valid UTF-8 encoding"""


def validUTF8(data):
    """determines if given data set reps valid UTF-8 encoding"""
    b = 0
    m = 1 << 6
    for x in data:
        mask = 1 << 7
        if b == 0:
            while x & mask:
                b += 1
                mask = mask >> 1
            if b > 4 or b == 1:
                return False
            if b == 0:
                continue
        else:
            if not (x & mask and not (x & m)):
                return False
        b -= 1
    return b == 0
