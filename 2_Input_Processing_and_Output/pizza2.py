"""
Adds the number of slices of pizzas 4 people eat and determines the number of whole pizzas 
required and the number of slices left over. No loops or lists or functions are used for 
this program. 

Args:
	p1NumberOfSlice (int): The number of slices first person will eat.
    p2NumberOfSlice (int): The number of slices second person will eat.
    p3NumberOfSlice (int): The number of slices third person will eat.
    p4NumberOfSlice (int): The number of slices fourth person will eat.
	
Outputs:
	wholePizzas (int): The number of whole pizzas to order.
	leftOverSlices (int): The number of slices left over. 

Assumptions:
	Every pizza has 8 slices.
	Everyone eats a different number of slices.
	If a negative number is entered, the program will exit. 
"""
PIZZA_SLICES = 8

print("Welcome to the 4 Person Pizza Calculator 2!")

try:
    p1NumberOfSlices = int(input("Enter the number of slices the first person will eat: "))
    p2NumberOfSlices = int(input("Enter the number of slices the second person will eat: "))
    p3NumberOfSlices = int(input("Enter the number of slices the third person will eat: "))
    p4NumberOfSlices = int(input("Enter the number of slices the fourth person will eat: "))
except:
    print("You must enter a number.")
    exit()

if p1NumberOfSlices < 0 or p2NumberOfSlices < 0 or p3NumberOfSlices < 0 or p4NumberOfSlices < 0:
    print("You must not enter a negative number.")
    exit()

totalSlices = p1NumberOfSlices + p2NumberOfSlices + p3NumberOfSlices + p4NumberOfSlices

numberWholePizzas = totalSlices // PIZZA_SLICES

if totalSlices % PIZZA_SLICES != 0:
    numberWholePizzas += 1

numberLeftOverSLices = totalSlices % PIZZA_SLICES

print("Total number of slices eaten:", totalSlices)
print("Total number of pizzas needed:", numberWholePizzas)
print("Total number of slices left over:", numberLeftOverSLices)
