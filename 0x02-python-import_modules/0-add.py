#!/usr/bin/python3
"""Can only work if you set name to main"""
if __name__ == "__main__":

    from add_0 import add
    a = 1
    b = 2

"""Use print .format style"""
print("{} + {} = {}".format(a, b, add(a, b)))
