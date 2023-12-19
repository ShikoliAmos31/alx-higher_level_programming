#!/usr/bin/python3
"""Module for MagicClass"""

import math


class MagicClass:
    """A magical class for handling radius and calculating area/circumference."""

    def __init__(self, radius):
        """
        Initialize MagicClass with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
        """
        self.__radius = 0

        if type(radius) not in (int, float):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
