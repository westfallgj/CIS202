class Shapes:
    """Represents a shape that can return its area

    Attributes:
        area (float): The area of a shape

    Methods:
        __str__ returns a string representation of the object's state
    """

    def __init__(self):
        self.__area = 0.0

    def area(self):
        pass

    def get_area(self):
        """Returns the area of the shape
        """
        return self.__area

    def __str__(self):
        return str(self.__area)

class Square(Shapes):
    """Represents a square shape that can return its area

    Attributes:
        area (float): The area of a shape
        side (float): length of one side of the square

    Methods:
        area: calculates and returns the area of the square
    """

    def __init__(self, side):
        Shapes.__init__(self)
        self.__side = side
    
    def area(self):
        self.__area = self.__side ** 2
        return self.__area

    def __str__(self):
        return str(self.__area)
    
class Triangle(Shapes):
    """Represents a triangle shape that can return its area

    Attributes:
        area (float): The area of a shape
        base (float): length of the triangle base
        height (float): height of the triangle

    Methods:
        area: calculates and returns the area of the triangle
    """

    def __init__(self, base, height):
        Shapes.__init__(self)
        self.__base = base
        self.__height = height
   
    def area(self):
        self.__area = ((self.__base * self.__height)/2)
        return self.__area

    def __str__(self):
        return str(self.__area)