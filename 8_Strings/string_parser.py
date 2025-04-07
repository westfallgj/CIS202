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
    """
    Reads a single line of x names from (const INPUT_FILE) in the format: "<firstname> <lastname>,"
    Strips the return (\n)
    Splits the line string into separate names based on ',' to create a list of names
    
        Args:
            none

        Returns:
            list of full names
    """
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
    """
    Creates a list of last names
        
        Args:
            a list of names to be ordered

        Return: 
            a list of last names
    """
    return name_list.split()[-1]

# docstring convention to use help()
if __name__ == "__main__":

    # Call to read input file
    names_list = read_input_file()
    print()
    print("Names List") 
    print(names_list)
    print()

    # sort names, using the get_last_name function in the iteration
    sorted_names = sorted(names_list, key=get_last_name)

    print("Ordered Names List")
    for name in sorted_names:
        first_name, last_name = name.split()
        print(f"{last_name}, {first_name}", end="; ")
    print()