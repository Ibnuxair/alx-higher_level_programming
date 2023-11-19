#!/usr/bin/python3
"""
This script lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    query = (
        "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    for city in cities:
        print(city[0])

    cursor.close()
    db.close()
