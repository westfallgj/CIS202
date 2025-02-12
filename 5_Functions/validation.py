"""
    Asks user input for hours and minutes. Validates the correctness of the input.
    Prints out the hours adn minutes after validation. 

    Output: correctly entered hours, minutes
"""

def input_check():
    """
    Checks the validity of hours (0-23) and minutes (0-59) entered by users.
    Asks for correct input if either variable is out of bounds.
    Arguments: none
    Outputs: correct hours_entered, minutes_entered
    """
    hours_entered = int(input("Enter hours (0-23): "))

    while (hours_entered < 0 ) or (hours_entered > 23):
        hours_entered = int(input("Error: value out of range (0-23): "))
    
    minutes_entered = int(input("Enter minutes (0-59): "))

    while (minutes_entered < 0) or (minutes_entered > 59):
        minutes_entered = int(input("Error: value out of range (0-59): "))
    
    return hours_entered, minutes_entered

hours, minutes = input_check()
print("You enetered ", hours, " hours, and ", minutes, "minutes")
print(f"You entered {hours} hours and {minutes} minutes.")
