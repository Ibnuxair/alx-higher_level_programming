#!/usr/bin/python3

"""
This script takes in an argument and displays all values in the states table of

hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    query = (
        "SELECT MIN(states.id), states.name "
        "FROM states "
        f"WHERE name LIKE  '{state_searched}'"
        "GROUP BY states.name "
        "ORDER BY MIN(states.id) ASC"
    )
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
