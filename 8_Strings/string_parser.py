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

def main():

    names_list = ()
    reversed_names_list = ()
    alpha_names_list = ()
    sorted_names_list = ()    
    

    names_list = read_test_input_file()
    print("NAMES LIST")
    print(names_list)

    reversed_names_list = reverse_name(names_list)
    print("Reversed NAMES LIST")
    print(reversed_names_list)
    
    alpha_names_list = alpha_order(reversed_names_list)
    print("alpha_sort process returns")
    print(alpha_names_list)

    reversed_names_list = reverse_name(alpha_names_list)
    print("reverse list again")
    print(reversed_names_list)


def read_test_input_file():
    """Gather input to  a list and return."""

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
 
def reverse_name(list_to_sort):
    """Sorts a list of names by the last name"""
    full_names_list = []
    this_name = []

    for full_name in list_to_sort:
        this_name = full_name.split()
        full_names_list.append(this_name[1] + " " + this_name[0])
    
    return full_names_list

def alpha_order(unordered_list):
    """ something """
    ordered_list = []

    for names in unordered_list:
        tokens = names.split(" ")
        ordered_list.append(tokens[1]+ " " + tokens[0])

    return ordered_list

# Call main function
main()