#!/usr/bin/python3
"""This script lists all states starting with letter 'N' """

import MySQLdb
import sys


def list_states(credentials):
    """Lists all states that start with letter 'N' ordered by ID

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

    cursor = db.cursor()
    query = "SELECT name FROM states ORDER BY id;"
    cursor.execute(query)

    rows = cursor.fetchall()
    for index, row in enumerate(rows):
        if (row[0].startswith('N')):
            state = (index + 1, row[0])
            print(state)


if __name__ == "__main__":
    credentials = sys.argv[1:]
    list_states(credentials)
