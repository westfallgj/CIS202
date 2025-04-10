import sqlite3

def main():
    db_connect = sqlite3.connect('customers.db')     # create/connect to the database
    db_cursor = db_connect.cursor()     # create a cursor to the database

    # Create table Customer in customers.db
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (ContactID INTEGER PRIMARY KEY NOT NULL,
                                                              Name TEXT NOT NULL, 
                                                              Email TEXT NOT NULL, 
                                                              SalesAmount REAL ) ''')
   
    # Insert customer data into the Customers table if it does not already exist
    db_cursor.execute('''INSERT OR IGNORE INTO Customers (ContactID, Name, Email, SalesAmount)
                         VALUES (1, "John Doe", "john.doe@example.com", 1000), 
                                (2, "Jane Smith", "jane.smith@example.com", 2000),
                                (3, "Fon Due", "fon.due@example.com", 3000)''')
    
    # Commit changes to customer database
    db_connect.commit() 

    # Select everything from the database
    db_cursor.execute('''SELECT * FROM Customers''')
    all_customers = db_cursor.fetchall()
    print(all_customers)

    # Print everything formatted
    for row in all_customers:
        print(f'{row[0]:5}, {row[1]:15}, {row[2]:15}, {row[3]:6}')

    # Select all Name, Email entries for Customers database
    db_cursor.execute('''SELECT Name, Email 
                          FROM Customers''')
    all_customers_names = db_cursor.fetchall()
    print(all_customers_names)

    # Select specific entry for Customers database
    db_cursor.execute('''SELECT Name, Email, SalesAmount 
                         FROM Customers 
                         WHERE Name == "John Doe"''')
    specific_customers_names = db_cursor.fetchall()
    print(specific_customers_names)

    # Update Customers table
    # db_cursor.execute('''UPDATE Customers 
    #                      SET Email == "fake email" 
    #                      WHERE Name == "John Doe"''')
    # db_connect.commit()
    # db_cursor.execute('''SELECT Name, Email, SalesAmount 
    #                      FROM Customers 
    #                      WHERE Name == "John Doe"''')
    # new_customers_email  = db_cursor.fetchall()
    # print(new_customers_email)

    db_connect.close()      # close the connection to the database

# main function
if __name__ == '__main__':
    main()