#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """defines the rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle class
        Args:
            width: represents the widht of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: If the size is not an integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle's area"""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the perimeter of a triangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """ Displays a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
        if column < self.__height - 1:
            rectangle += "\n"
        return (rectangle)
