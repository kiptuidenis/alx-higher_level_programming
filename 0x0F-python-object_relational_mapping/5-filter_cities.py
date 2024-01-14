#!/usr/bin/python3
"""This script takes lists all cities of a state"""

import MySQLdb
import sys


def list_cities_of_states(credentials):
    """Lists the all cities of the state specified by the user

    Args:
        credentials (str): Credentials of the database from which the cities\
        are to be listed. Includes the name of the state
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=credentials[0],
        password=credentials[1],
        db=credentials[2]
    )

    cursor = db.cursor()
    state_name = credentials[3]
    query = "SELECT cities.name\
        FROM states INNER JOIN cities\
            ON states.id = cities.state_id\
                WHERE states.name LIKE BINARY %s\
                    ORDER BY cities.id;"
    
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    separator = ", "
    if len(rows) == 0:
        print("")
    for index, row in enumerate(rows):
        print("{}{}".format(row[0], separator), end="")
        if index == len(rows) - 2:
            separator = "\n"
    cursor.close()
    db.close()


if __name__ == "__main__":
    credentials = sys.argv[1:]
    list_cities_of_states(credentials)
