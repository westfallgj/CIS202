 

def main():
    # Variables
    totalsales = 0.0
    salesinput = open('sales.txt', 'r')

    # Initialize lists
    daily_sales = salesinput.readlines()
    #print(daily_sales)
    
    for i in daily_sales:
        totalsales = totalsales + int(i)
    maxsales = max(daily_sales)

    uniqsales = set(daily_sales)
    #print(uniqsales)
    print("The elememts of the set are: ")
    for i in uniqsales:
        print(int(i), end = " ")
    print()
    
    # Display total sales
    print (f'Total sales for the week: ${totalsales:,.2f}')
    print(f'The maximum sales for the week: ${int(maxsales):,.2f}')

# Call the main function.
main()
