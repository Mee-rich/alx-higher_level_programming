#!/usrbin/python3
"""
This script lists all states with a `name` starting
with the letter `N` from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database after MYSQL credentials
    are satisfied.
    """
    db = MYSQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
