#!/usr/bin/python3

def max_integer(my_list=[]):
    if (my_list):
        list_max = -1
        for i in range(len(my_list)):
            if (my_list[i] > list_max):
                list_max = my_list[i]
        return (list_max)
    else:
        return None
