import sqlite3

def main():
    """
    Connects to the 'customers.db' database, adds initial customers, and performs various queries.
    """
    # create/connect to the database
    db_connect = sqlite3.connect('customers.db')     
    # create a cursor to the database
    db_cursor = db_connect.cursor()     

    add_initial_customers(db_cursor)
    db_connect.commit()

    print_all_customers(db_cursor)

    print_greater_than_1000_sales(db_cursor)

    query_min_sales(db_cursor)

    # close the connection to the database
    db_connect.close()      

def query_min_sales(curses):
    """
    Queries and prints customers with sales amounts greater than a user-specified minimum.

    Args:
        curses: The cursor object for database interaction.
    """   
    # query user
    min_sales = input("\nEnter minimum sales: ")

    # Select everything from the database
    curses.execute('''SELECT Name, SalesAmount FROM Customers WHERE SalesAmount > ?''', (min_sales,))
    all_customers = curses.fetchall()

    # print proper format
    print("Customers with sales greater than ", min_sales)
    for name, sales in all_customers:
        print(f"{name:15} {sales:6.2f}")

    return

def print_greater_than_1000_sales(curses):
    """
    Queries and prints customers with sales amounts greater than 1000.

    Args:
        curses: The cursor object for database interaction.
    """
    # Select from the database
    curses.execute('''SELECT Name, SalesAmount FROM Customers WHERE SalesAmount > 1000''')
    all_customers = curses.fetchall()

    # print proper format
    print("\nCustomers with sales greater than 1000")
    for name, sales in all_customers:
        print(f"{name:15} {sales:6.2f}")

    return

def print_all_customers(curses):
    """
    Queries and prints all customers from the Customers table.

    Args:
        curses: The cursor object for database interaction.
    """
    # Select everything from the database
    curses.execute('''SELECT * FROM Customers''')
    all_customers = curses.fetchall()

    # print proper format
    print("\nAll customers:")
    print(all_customers)

    return

def add_initial_customers(curses):
    """
    Adds initial customer data to the Customers table if it doesn't exist.

    Args:
        curses: The cursor object for database interaction.
    """
    # A list of customers
    customers = [(1, "John Doe", "john.doe@example.com", 1000),
                 (2, "Jane Smith", "jane.smith@example.com", 2000),
                 (3, "Fon Due", "fon.due@example.com", 3000)]

    # Create table Customer in customers.db
    curses.execute('''CREATE TABLE IF NOT EXISTS Customers (
                   ContactID INTEGER PRIMARY KEY NOT NULL,
                   Name TEXT NOT NULL, 
                   Email TEXT NOT NULL, 
                   SalesAmount REAL
                ) ''')

    # print in proper format
    for row in customers:
        curses.execute('''INSERT OR IGNORE INTO Customers (ContactID, Name, Email, SalesAmount)
                       VALUES (?, ?, ?, ?)''', (row[0], row[1], row[2], row[3]))
    return

# main function
if __name__ == '__main__':
    main()