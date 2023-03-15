#!/usr/bin/python3

def best_score(a_dictionary):
    if(a_dictionary):
        maxi = -1
        for val in a_dictionary.values():
            if val > maxi:
                maxi = val

        for key in a_dictionary.keys():
            if a_dictionary[key] == maxi:
                return key

    else:
        return None
