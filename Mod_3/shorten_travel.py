"""
    Calculates amount of time saved if you are traveling with an average speed that 
    is above the speed-limit as compared to traveling at exactly at the speed-limit. 

    Args:
	    averageSpeedMPH (float): the average speed in miles per hour
        speedLimitMPH (float): the speed limit in miles per hour
        distanceTraveled (float): the distance traveled
	
    Outputs:
	    minutesSaved (float): the time saved in minutes

    Assumptions:
	    All speeds are in MPH.
        All distances are in miles. 
"""
MINUTES_IN_HOUR = 60

print("Welcome to Shorten Travel")

averageSpeedMPH = float(input("Enter the average speed you will travel in MPH: "))
speedLimitMPH = float(input("Enter the speed limit in MPH: "))
distanceTraveled = float(input("Enter the distance traveled in miles: "))

# what are the use cases for a control?
#   if any input <= 0, then no time is saved
#   if averageSpeedMPH <= speedLimitMPH, then no time is saved
if ((averageSpeedMPH  <= 0) or (distanceTraveled <= 0) or (speedLimitMPH <= 0) or
        (averageSpeedMPH <= speedLimitMPH)):
    print("No time will be saved")
else:
    normalTimeInHours = round((distanceTraveled / speedLimitMPH), 2)
    reducedTimeInHours = round((distanceTraveled / averageSpeedMPH), 2)
    hoursSaved = round((normalTimeInHours - reducedTimeInHours), 2)
    minutesSaved = int(hoursSaved * MINUTES_IN_HOUR )
    print(minutesSaved, "minutes saved.")
