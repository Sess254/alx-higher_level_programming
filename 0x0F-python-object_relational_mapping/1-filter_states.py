#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N)"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], port=3306)

    curs = db.cursor()
    curs.execute("SELECT * \
    FROM states \
    WHERE CONVERT(name USING Latin1) \
    COLLATE Latin1_General_CS \
    LIKE 'N%';")
    states = curs.fetchall()

    for state in states:
        print(state)
