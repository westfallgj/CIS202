# Declare variables
numTotal = numMaximum = numAverage = numUnique = numGT200 = 0
input_list = []

try:

    inputFile = open("numbers-1.txt")

    # Grab the numbers and store in a list
    for line in inputFile:
        num = line.rstrip("\n")
        input_list.append(num)

    # find the total and print to the screen
    for num in input_list:
        numTotal += int(num)
    
    print("The total is: " + str(numTotal))

    # calculate the maximum and print to the screen
    for num in input_list:
        if int(num) > numMaximum:
            numMaximum = int(num)
    
    print("The maximum is: " + str(numMaximum))

    # calculate the average and print to the screen
    numAverage = numTotal / len(input_list)
    print("The average is: " + str(numAverage))

    # calculate the unique numbers
    for num in input_list:
        if input_list.count(num) == 1:
            numUnique += 1

    # find numbers greater than 200
    for num in input_list:
        if int(num) > 200:
            numGT200 += 1

    print("The total numbers in the list grater than 200 is: " + str(numGT200))

except IOError:
    print("IOError: the numbers-1.txt file cannot be found in this directory")

