"""
    Adds the number of slices of pizzas 4 people eat and determines the number of whole 
    pizzas required and the number of slices left over. No loops or lists or functions 
    are used for this program. 

    Args:
	    numberOfSlices (int): The number of slices each person will eat.
	
    Returns:
	    wholePizzas (int): The number of whole pizzas to order.
	    leftOverSlices (int): The number of slices left over. 

    Assumptions:
	    Every pizza has 8 slices.
	    Everyone eats the same number of slices.
        If a negative number is entered, the program will exit. 
"""
PIZZA_SLICES = 8
PEOPLE = 4

print("Welcome to the 4 Person Pizza Calculator!")

try: 
    numberOfSlices = int(input("Enter the number of slices each person will eat: "))    # get number of slices and cast to int
except:
    print("You must enter a number.")
    exit()

if numberOfSlices < 0:  # check for incorrect input
    print("You must not enter a negative number.")
    exit()

totalSlices = PEOPLE * numberOfSlices
numberWholePizzas = totalSlices // PIZZA_SLICES

if totalSlices % PIZZA_SLICES != 0:
    numberWholePizzas += 1

numberLeftOverSLices = totalSlices % PIZZA_SLICES

print("Total number of slices eaten:", totalSlices)
print("Total number of pizzas needed:", numberWholePizzas)
print("Total number of slices left over:", numberLeftOverSLices)
