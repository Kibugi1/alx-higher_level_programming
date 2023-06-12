#!/usr/bin/python3
def no_c(my_string):
    string_new = my_string.translate({ord(i): None for i in 'cC'})
    return string_new
