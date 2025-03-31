import shapes

def main():
    """
    This program demonstrates the functionality of the 'shapes' module,
    which defines classes for different geometric shapes (currently Square and Triangle).
    """

    # instantiate the shapes
    square1 = shapes.Square(3.0)
    triangle1 = shapes.Triangle(4, 5)

    # calculate/print the different shapes areas
    print(square1.area())
    print(triangle1.area())

    # Test string representation of the objects
    print(square1)
    print(triangle1)

# Call the main function
main()