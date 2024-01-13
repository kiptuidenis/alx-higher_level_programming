#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys

def list_states(credentials):
    """lists all states ordered by their ids

    Args:
        credentials (string): database credentials
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=credentials[0],
        password=credentials[1],
        db=credentials[2]
    )

    cursor = db.cursor()
    query = "SELECT name FROM states ORDER BY id;"
    cursor.execute(query)

    rows = cursor.fetchall()
    i = 0
    for row in rows:
        i += 1
        state = (i, row[0])
        print(state)

if __name__ == "__main__":
    credentials = sys.argv[1:]
    list_states(credentials)
