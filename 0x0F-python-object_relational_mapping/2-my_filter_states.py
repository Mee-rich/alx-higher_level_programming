#!/usr/bin/python3
"""
This script takes in an argument and displays
all values in the states where `name` matches
the argument from the database `htbn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database after MYSQL injections
    are satisfied.
    """
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3],
            host="localhost", port=3306)
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)
