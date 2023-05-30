#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        r = fct(*args)
    except Exception as err:
        r = None
        print("Exception: {}".format(err), file=stderr)
    finally:
        return r
