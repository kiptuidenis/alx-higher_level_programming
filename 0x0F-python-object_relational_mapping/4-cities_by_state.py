#!/usr/bin/python3
"""This script lists all cities from the database"""

import MySQLdb
import sys


def list_cities(credentials):
    """Lists all cities in a state

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
    query = (
        "SELECT cities.id, cities.name, states.name\
            FROM states INNER JOIN cities\
                ON states.id = cities.state_id\
                    ORDER BY cities.id;"
    )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    credentials = sys.argv[1:]
    list_cities(credentials)
