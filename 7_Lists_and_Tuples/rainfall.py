"""
    Calculates the total rainfall, average monthly rainfall, and months with highest/lowest rainfall
    for 12 months of rainfall date entered by the user.
    
    Handles ValueError exceptions that are raised when the items that are entered by the user are 
    converted to a number.

    Args:
        muffinCount (int): 

    Outputs:
	    Total, average, highest (name and amount), and lowest (name and amount) months of rainfall.
        IOError and/or ValueError exceptions, when raised.
"""
import matplotlib.pyplot as plt


### pushing update

# make a tuple of the months
months_list = ('January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December')

def getInputData():

    try:
        input_list = []
        
        for month in months_list:
            input_list.append(input("Enter the monthly rainfall for " + month + ":"))

        return input_list

    except ValueError:
        print("Value error: expected the name of a month (string)")

def findAverage(rainfall_list):
    average = 0

    for amount in rainfall_list:
        average += float(amount)

    average = average / len(rainfall_list)

    return average

rainfall_list = getInputData()
average_rainfall = findAverage(rainfall_list)

print(rainfall_list)
print("Average rainfall was", round(average_rainfall, 2), "inches.")
print("The minimum rainfall was", min(rainfall_list))
print("The maximum rainfall was", max(rainfall_list))

# make a list to get the 12 values months.append(value)
# mean() function to get the average
# min()/max() function will find greatest and least but I need the index
# use index(MAX or MIN rainfall) to get the index that will = the month
# print index(MAN or MIN) has the most rain, amount of rain
# plt.plot(avgRainFall, months)
# plt.title('Average Rainfall')
# plt.ylabel('Rainfall (inches))
# plt.xlabel('Month')
# plt.xlim() to add space?
# plt.xticks(create a list of length Month, Months)
# plt.grid(True)
plt.show()

'''
a = [3, 5, 7, 2, 8, 1]

# Find the maximum element
mxv = max(a)

# Find the position of maximum element
mxp = a.index(mxv)

# Find the minimum element
mnv = min(a)

# Find the position of minimum element
mnp = a.index(mnv)

print(mxp)
print(mnp)
'''