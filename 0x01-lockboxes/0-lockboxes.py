#!/usr/bin/python3
"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if the boxes can be opened.
    """
    for key in range(1, len(boxes) - 1):
        ctr = False
        for idx in range(len(boxes)):
            ctr = (key in boxes[idx] and key != idx)
            if ctr:
                break
        if ctr is False:
            return ctr
    return True
