#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except ValueError as err1:
        print("Exception: {}".format(err1), file=stderr)
        return False
    except ValueError as err2:
        print("Exception: {}".format(err2), file=stderr)
        return False
    else:
        return True
