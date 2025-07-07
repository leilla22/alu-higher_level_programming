#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Defines a square """

    def __init__(self, size=0, position=(0, 0)):
        "" initializing the variables """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """returning the value of the size """
        return self.__size

    @size.setter
    def size(self, size):
        """setting the value of size """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must begreater than or equal to 0")
        else:
            self.__size = size

    def area(self):
        square_area = self.__size ** 2
        return square_area

    def __init__(self, size=0, position=(0, 0)):
        """ initializing the data """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """showing position of the size """
        return self.__position

    @position.setter
    def position(self, value):
        """setting position """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ printing a # square according to the size value """
        if self.size == 0:
            print("")
            return

        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
