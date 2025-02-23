"""
    Calculates the sum and average of numbers stored in the provided file, "numbers.txt". Handles any IOError exceptions that are raised when the file is opened and data is read  from file. Handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.

    Args:
        None

    Outputs:
	    Sum and Average of all numbers.
        IOError and/or ValueError exceptions, when raised.
"""
# Declare varaibles for sum
numSum = numItems = 0

try:
    # Open input file: numbers.text
    inputFile = open("numbers.txt", 'r')

    # Grab the individual numbers and strip
    for num in inputFile:
        num = num.rstrip("\n")
        numSum += float(num)
        numItems += 1

    print(f"The sum of the numbers is: {numSum:.2f}")
    print(f"The average of the numbers is: {(numSum/numItems):.2f}")

    # Close input file
    inputFile.close()

except IOError:
    print("IOError: the numbers.txt file cannot be found in this directory.")
except ValueError:
    print("Value error: there is a problem with one or more values from inputFile.")
