#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Class with public instance methods"""

    def area(self):
        """Raises an Exception with the message
        'area() is not implemented'
        """
         raise Exception(" area() is not implemented")

     def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
