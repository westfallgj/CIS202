"""
    Calculates the number of muffins and/or cupcakes sold at the bakery. 
    Assumes a stock of 10 cupcakes and 10 muffins.

    Args:
        muffinCount (int): number of muffins to start
        cupcakeCount (int): number of cupcakes to start
        choice (string): the customer choice of 'muffin'/'cupcake' 
            or '0' to end the program

    Outputs:
	    muffinCount, cupcakeCount: the count of items left
"""
muffinCount = 10    # number of muffins to start
cupcakeCount = 10   # number of cupcakes to start

# ask for target variable
choice = input("What would you like, a muffin or a cupcake (0 to end): ")

# check input for '0'
while  (choice != '0') and (muffinCount != 0) and (cupcakeCount != 0):
    if choice == 'muffin':
        if (muffinCount != 0):
            muffinCount -= 1
    elif choice == 'cupcake':
        if (cupcakeCount != 0):
            cupcakeCount -= 1
    else:
        print("Invalid input")      
    # ask for new input
    choice = input("What would you like, a muffin or a cupcake (0 to end): ")

# end program
print("muffins:", muffinCount, "cupcakes:", cupcakeCount)
print("End Program")
