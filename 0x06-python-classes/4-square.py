#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """
    Square class with private instance attribute size.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance with a given size.
        area(self): Computes the area of the square.
        size(self): Getter method for __size.
        size(self, value): Setter method for __size.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for __size.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for __size.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
