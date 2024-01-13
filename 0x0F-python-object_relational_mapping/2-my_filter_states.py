#!/usr/bin/python3
"""This script lists all states searched by user"""

import MySQLdb
import sys


def list_states(credentials):
    """Selects and lists all states specified by user

    Args:
        credentials (str): Database credentials
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=credentials[0],
        password=credentials[1],
        db=credentials[2]
    )

    state_name = credentials[3]
    cursor = db.cursor()
    query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id;".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    credentials = sys.argv[1:]
    list_states(credentials)
