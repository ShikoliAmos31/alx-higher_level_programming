#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class MyInt(int):
    """Class representing a custom integer type."""

    def __eq__(self, other):
        """Override equality comparison."""
        return int(self) != other

    def __ne__(self, other):
        """Override inequality comparison."""
        return int(self) == other


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
