#!/usr/bin/python3
# 0-square.py by UDO INNOCENT
"""A module that defines a square in the code """


class Square:
    """A class that reps in a square"""

    def __init__(self, size=0):
        """Initializes  square class in the code
        Args:
            size: reps the size of the square defined
        Raises:
            TypeError: if size isn't int
            ValueError: if size is < zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an int')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
