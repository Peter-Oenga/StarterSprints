class Rectangle:
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        

    @property
    def width(self):
        return self.__width
    
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
    
    def area(self):
        return self.__width * self.__height
    
    def perimeter(self):
        if self.__width != 0 or self.__height != 0:
            result = 2 * (self.__width + self.__height )
            return result
        else:
            return 0
    
    
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""

        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))