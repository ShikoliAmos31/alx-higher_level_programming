#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor object to interact with the database
    cursor = db.cursor()

    # Execute MySQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows and print them
    for state in cursor.fetchall():
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
