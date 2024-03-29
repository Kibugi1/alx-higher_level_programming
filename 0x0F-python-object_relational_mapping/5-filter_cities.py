#!/usr/bin/python3
"""
This script takes in the name of a state as an argument
and lists all cities of that state, using the database
hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    arg = sys.argv[4]
    cur = db.cursor()
    cur.execute('SELECT cities.name \
                FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %(name)s', {'name': arg})

    cities = cur.fetchall()
    list_cities = [item for city in cities for item in city]
    print(", ".join(list_cities))

    cur.close()
    db.close()
