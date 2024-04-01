#!/usr/bin/python3
"""Module documentation for Square class."""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initialize a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
