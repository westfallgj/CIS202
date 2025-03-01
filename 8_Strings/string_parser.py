"""
    Reads a string from the user containing a list of names separated by commas and spaces. 
    The program should then parse the string and print the names in alphabetical order in 
    the format:
    
        "Last Name, First Name" in alphabetical order.
    
    Handles ValueError exceptions that are raised when the items that are entered by the user are 
    converted.

    Args:
        names (string): user input, string of formatted names

    Outputs:
	    Total, average, highest (name and amount), and lowest (name and amount) months of rainfall.
        IOError and/or ValueError exceptions, when raised.
"""
INPUT_FILE = "test_file.txt"
names_list = ()

def read_test_input():
    
    try:
        # Open input file
        input_file = open(INPUT_FILE, 'r')

        for line in input_file:
            #print(line)
            # Grab the individual numbers and strip
            input_list = ()

        # Close input file
        input_file.close()

        return input_list
    
    except IOError:
        print("IOError: the input file cannot be found.")
    
def gather_input():

    return input_list

names_list = read_test_input()