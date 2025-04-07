import sqlite3

def main():
    db_connect = sqlite3.connect('contacts.db')     # create the database
    db_cursor = db_connect.cursor()     # create a cursor to the database

    # Insert code here to perform operations on the database.

    # format to SWL statement execution
    # db_cursor.execute(SQLstring)
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Test (Name TEXT, ID INTEGER PRIMARY KEY NOT NULL) ''')
    
    person_name = "Konner"
    person_id = 2
    db_cursor.execute('''INSERT INTO Test (Name, ID)
                          VALUES ("Josh", 1),
                                 ("Kash", 3)''')
    db_cursor.execute('''INSERT INTO Test (Name, ID)
                          VALUES (?, ?)''', (person_name, person_id))
    
    db_connect.commit()     #saves changes to the db

    db_cursor.execute('''DROP TABLE IF EXISTS Test''')

    db_connect.commit()     #saves changes to the db
    db_connect.close()      # close the connection to the database

# main function
if __name__ == '__main__':
    main()