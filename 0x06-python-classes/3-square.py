#!/usr/bin/python3
"""
    square class
"""


class Square:
    """Defines  a square class"""

    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
