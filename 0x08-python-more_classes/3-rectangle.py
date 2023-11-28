#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
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
        """Gets the height of e rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an int")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self) -> str:
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
        [rect.append('#') for j in range(self.__width)]
        if i != self.__height - 1:
            rect.append("\n")
        return ("".join(rect))
