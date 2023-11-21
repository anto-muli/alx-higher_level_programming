#!/usr/bin/python3
"""proceudre 4 a docstring"""
import math


class MagicClass:
    """sets up e magic"""

    def __init__(self, radius=0):
        """ writing a 2nd docstring """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a #')
        self.__radius = radius

    def area(self):
        """another docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """such docstring"""
        return 2 * math.pi * self.__radius
