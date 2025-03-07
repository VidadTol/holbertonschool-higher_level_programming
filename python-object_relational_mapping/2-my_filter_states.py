#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
    """

import MySQLdb
import sys


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa
        """

    # Connect to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
            charset="utf8",
            port=3306
            )
    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states WHERE name \
                LIKE BINARY '{}%' ORDER BY id ASC".format(sys.argv[4]))

    # Fetch all the rows from the executed query
    rows = cur.fetchall()

    # print each row
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cur.close()
    db.close()
