#!/usr/bin/python3
from sys import argv
j = 0
if __name__ == "__main__":
    if len(argv) == 1:
        print("{}".format(int(j)))
    else:
        for i in range(1, len(argv)):
            j += int(argv[i])
        print("{}".format(int(j)))
