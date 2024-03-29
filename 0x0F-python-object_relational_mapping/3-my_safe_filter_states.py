#!/usr/bin/python3
"""script that takes in arguments and
   displays all values in the states table of hbtn_0e_0_usa
   where name matches the argument. But this time,
   write one that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curs = db.cursor()
    curs.execute("SELECT * FROM states WHERE name = %s;", (sys.argv[4],))
    states = curs.fetchall()

    for state in states:
        print(state)
