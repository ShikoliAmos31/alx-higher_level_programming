#!/usr/bin/python3
"""Module defining a Square class."""


class Square:
    """Square class with private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Override the equality operator."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Override the inequality operator."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Override the less than operator."""
        return self.area() < other.area()

    def __le__(self, other):
        """Override the less than or equal to operator."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Override the greater than operator."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Override the greater than or equal to operator."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
