#!/usr/bin/python3
""" Defining a square """


class Square:
    """ Defining a square and creates a private instance attribute """
    def __init__(self, size=0):
        """ initializing size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than or equal to 0")
        else:
            self.__size = int(size)

    def area(self):
        square_area = self.__size ** 2
        return square_area
