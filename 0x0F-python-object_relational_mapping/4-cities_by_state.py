#!/usr/bin/python3
"""Lists all states from the hbtn_0e_o_usa database. """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials
    
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    # Connect to MySQL server
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
            FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")

    # Fetch all rows and print the states
    [print(city) for city in cursor.fetchall()]
