#!/usr/bin/env python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
    """
import MySQLdb
import sys


if __name__ == "__main__":
    def list_states():
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
        cur.execute("SELECT * FROM states \
                    WHERE BINARY LIKE 'N%' ORDER BY id ASC")

        # Fetch all the rows from the executed query
        rows = cur.fetchall()

        # print each row
        for row in rows:
            print(row)

        # Close the cursor and the database connection
        cur.close()
        db.close()

    list_states()