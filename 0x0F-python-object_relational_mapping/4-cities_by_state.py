#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name \
    From cities JOIN states ON cities.state_id = states.id;")
    states = curs.fetchall()

    for state in states:
        print(state)