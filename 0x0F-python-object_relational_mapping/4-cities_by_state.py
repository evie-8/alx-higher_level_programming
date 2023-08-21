#!/usr/bin/python3
'''Script that lists all states'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        sys.exit("You have passed few arguments")
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursors = db.cursor()
    result = cursors.execute("SELECT cities.id, cities.name, states.name "

                             "FROM cities "

                             "JOIN states ON cities.state_id = states.id "

                             "ORDER BY cities.id ASC")
    rows = cursors.fetchall()
    for row in rows:
        print(row)
    cursors.close()
    db.close()
