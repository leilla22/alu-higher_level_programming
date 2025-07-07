#!/usr/bin/python3
""" Defines a square """


class Square:
    """ creating a private instance attribute """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be greater than or equal to  0")
        else:
            self.__size = int(size)

    def area(self):
        square_area = self.__size ** 2
        return square_area

    @property
    def size(self):
        """returning the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """setting the size value of the square object """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be greater than or equal to 0")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.size)
