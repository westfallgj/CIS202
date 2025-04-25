def main():
    again = 'y'
    total = 0
    count = 0
    
    # Get scores
    while again == 'y':
        points = int(input('What was your score? '))
        total = total + points
        count = count + 1
        score = total/count
        grade = determine_grade(score)
        again = input('y for another score or any key to quit ')
    print(f"average score is {score:.2f}")
    print("Letter grade is ", grade)
   

# The determine_grade function receives a numeric  
# grade and returns the corresponding letter grade 
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Call the main function.
main()


