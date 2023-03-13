#!/usr/bin/python3

def no_c(my_string):
    for str in my_string:
        if str == 'c' or str == 'C':
            idx = my_string.find(str)
            my_string = my_string[:idx] + my_string[idx + 1:]
    return (my_string)
