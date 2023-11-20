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
        "SELECT DISTINCT id, name "
        "FROM states "
        "WHERE name COLLATE utf8mb4_bin LIKE '{}' "
        "ORDER BY id ASC"
    ).format(state_searched)
    cursor.execute(query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
