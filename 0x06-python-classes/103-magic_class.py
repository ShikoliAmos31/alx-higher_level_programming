#!/usr/bin/python3
"""
This module defines the MagicClass.

MagicClass has methods to initialize an instance with a radius, calculate the area,
and calculate the circumference.
"""

import math


class MagicClass:
    """
    MagicClass represents a class with methods to perform calculations based on the radius.

    Attributes:
    __radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
        radius (float): The radius of the circle.

        Raises:
        TypeError: If the provided radius is not a number.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
        float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
        float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
