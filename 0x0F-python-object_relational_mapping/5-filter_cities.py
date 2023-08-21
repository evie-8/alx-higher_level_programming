#!/usr/bin/python3
'''Script that lists all cities'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        sys.exit("You have passed few arguments")
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursors = db.cursor()
    result = cursors.execute("SELECT cities.id, cities.name, states.name "

                             "FROM cities "

                             "JOIN states ON cities.state_id = states.id "

                             "WHERE states.name = %s "

                             "ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cursors.fetchall()
    city = ", ".join(row[1] for row in rows)
    print(city)
    cursors.close()
    db.close()
