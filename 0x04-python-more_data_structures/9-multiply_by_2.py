#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    for key, val in new_dict.items():
        new_dict[key] = val * 2
    return new_dict
