#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Square class with private instance attributes: size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer or if position is not a tuple
                       of two positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Args:
            value (tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the character #.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    my_square = Square(5, (0, 0))
    my_square.my_print()

    print("--")

    my_square = Square(5, (4, 1))
    my_square.my_print()
