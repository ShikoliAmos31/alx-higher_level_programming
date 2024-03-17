#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Construct SQL query
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the SQL command
    cursor.execute(sql, (sys.argv[4],))

    # Fetch all the rows in a list of lists
    results = cursor.fetchall()

    # Print fetched result
    for row in results:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()
