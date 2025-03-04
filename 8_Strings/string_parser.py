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
sorted_list = ()

def read_input_file():
    """Gather/Stript/Split input file to a list and return."""
    try:
        # Open input file
        input_file = open(INPUT_FILE, 'r')

        for line in input_file:
            # strip the newline 
            line = line.rstrip("\n")
            # Grab the individual numbers and strip
            tokens = line.split(', ')
        
        # Close input file
        input_file.close()

        return tokens
    
    except IOError:
        print("IOError: the input file cannot be found.")
 
def get_last_name(name_list):
    """Creates/Returns a last name list. given a list of names"""
    return name_list.split()[-1]

# Call to read input file
names_list = read_input_file()
print("Names List", names_list)

# sort names, using the get_last_name function in the iteration
sorted_names = sorted(names_list, key=get_last_name)

for name in sorted_names:
    print(name)