#!/usr/bin/python3
"""
    Write a class Square that defines a square by:\
    (based on 3-square.py)

    Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
            - size must be an integer, otherwise raise a\
            TypeError exception with the message size must be an integer
            - if size is less than 0, raise a ValueError\
            exception with the message size must be >= 0
    Instantiation with optional size: def __init__(self, size=0):
    Public instance method: def area(self): that returns the\
    current square area
    You are not allowed to import any module
"""


class Square():

    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")

    def area(self):
        return self.__size * self._size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
