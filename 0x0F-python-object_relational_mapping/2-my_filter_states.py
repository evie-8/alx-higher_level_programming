#!/usr/bin/python3
'''Script that lists all states starting with letter N'''


if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        sys.exit("You have passed few arguments")
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    r = cur.execute("SELECT * FROM states WHERE states.name like BINARY '{}' "

                    "ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
