"""
Write a class Square that defines a square by: (based on 6-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integer
Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space
Printing a Square instance should have the same behavior as my_print()
You are not allowed to import any module
"""

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(coord, int) and coord >= 0 for coord in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
            return
        
        x, y = self.__position

        for _ in range(y):
            print()

        for _ in range(self.__size):
            print(" " * x, end="")
            print("#" * self.__size)


# Test the class
my_square = Square(5, (0, 0))
my_square.my_print()

print("--")

my_square = Square(5, (4, 1))
my_square.my_print()
