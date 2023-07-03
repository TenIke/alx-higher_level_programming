#!/usr/bin/python3
"""Define a class rectangle"""


class Rectangle:
    """Initialize a rectangle"""

    def __init___(self, width=0, height=0):
        """ New rectangle

        Args:
            Width = type int and it's the width of it
            Height = int and ithe the heigh
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Get the value of the width"""
            retrun self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
