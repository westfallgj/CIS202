"""
    Calculates the total rainfall, average monthly rainfall, and months with highest/lowest rainfall
    for 12 months of rainfall date entered by the user.
    
    Handles ValueError exceptions that are raised when the items that are entered by the user are 
    converted.

    Args:
        muffinCount (int): 

    Outputs:
	    Total, average, highest (name and amount), and lowest (name and amount) months of rainfall.
        IOError and/or ValueError exceptions, when raised.
"""
import matplotlib.pyplot as plt

# make a tuple of the months
months_list = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
                'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')

def get_input_data():
    """A function to gather input and return a list"""
    input_list = []
    
    try:
        for month in months_list:
            input_list.append(float(input("Enter the monthly rainfall for " + month + ":")))
        return input_list
    
    except ValueError:
        print("Value error: expected the number (integer)")

def find_total(rf_list):
    """a function to find and return the total of a list"""
    total = 0

    try:
        for amount in rainfall_list:
            total += float(amount)    
        return total
    
    except ValueError:
     print("Value error: could not convert string to a float")

def find_average(rf_list):
    """a function to find and return an average of a list"""
    average = 0

    try:
        for amount in rainfall_list:
            average += float(amount)    

        return average / len(rainfall_list)
    
    except ValueError:
     print("Value error: could not convert string to a float")

# get input
rainfall_list = get_input_data()
# calculate total
total_rainfall = find_total(rainfall_list)
# calculate average
average_rainfall = find_average(rainfall_list)

# grab the index of the rainfall minimum and maximum and use
# those values to get the correct element from the months_list
min_month = months_list[rainfall_list.index(min(rainfall_list))]
max_month = months_list[rainfall_list.index(max(rainfall_list))]

# print the required output
print("Total rainfall was", round(total_rainfall, 2))
print("Average rainfall was", round(average_rainfall, 2))
print("The minimum rainfall was", min(rainfall_list), "inches in", min_month)
print("The maximum rainfall was", max(rainfall_list), "inches in", max_month)

# trying some plotting 
plt.plot(months_list, rainfall_list)
plt.title('Yearly Average Rainfall by Month')
plt.ylabel('Rainfall (inches)')
plt.xlabel('Months')
plt.xticks(rotation= 45, ha='right')
plt.grid(True)
plt.tight_layout()
plt.show()

print("Rainfall program complete.")