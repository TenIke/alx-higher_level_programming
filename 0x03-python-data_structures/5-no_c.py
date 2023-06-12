#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for n in my_string:
        if n.lower() != 'c' and n.upper() != 'C':
            new_string += n
    return new_string
