class Square(Shape):

    """Represents a square shape that can returns it's area

    Attributes:
        area (float, hidden): The area of a shape

    Methods:
        __str__ returns objects state
    """

    def __init__(self):
        self.__area = 0.0

    def __str__(self):
        return str(self.__area)