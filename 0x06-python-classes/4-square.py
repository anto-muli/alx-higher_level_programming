#!/usr/bin/python3
"""
    square class
"""


class Square:
    """Defines a square in the class"""

    def __init__(self, size=0):
        """Initializes e square class
        Args:
            size: reps the size of the square defined
        Raises:
            TypeError: if size is not int
            ValueError: if size is < zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an int')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return (self.__size ** 2)
