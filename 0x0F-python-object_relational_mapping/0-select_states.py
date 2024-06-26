#!/usr/bin/python3
"""
This script lists all states from 
the database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    List all states by accessing the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
