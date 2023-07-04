#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """This function returns addition of a and b

    Float numbers should be typecasted to ints before addition takes place
    Raises a TypeError if a or b is nonfloat or noninteger
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
