#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """ initializing  the square object """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than or equal to 0")
        else:
            self.__size = int(size)
