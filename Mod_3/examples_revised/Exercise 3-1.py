# Programming Exercise 3-1
'''
Write a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week,
where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.
The program should display an error message if the user enters a number that is outside the range of 1 through 7.
'''

# Get the number for the day of the week.
day = int(input('Enter a number (1-7) for the day of the week: '))

# Determine the name of the day of the week, and display it.
if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print ('Thursday')
elif day == 5:
    print ('Friday')
elif day == 6:
    print ('Saturday')
elif day == 7:
    print ('Sunday')
else:
    print ('Error: Please enter a number in the range 1-7.')

print("over")



