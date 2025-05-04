# Declare variables
numTotal = numMaximum = numAverage = numUnique = numGT200 = 0
input_list = []

try:
    # Open the input file
    input_file = open("numbers-1.txt", 'r')

    for line in input_file:
        num = line.rstrip("\n")
        input_file. append(num)

except IOError:
    print("IOError: the numbers-1.txt file cannot be found in this directory")