#!/usr/bin/python3

def no_c(my_string):
    for str in my_string:
        if str == 'c' or str == 'C':
            str = ''
    return (my_string)
