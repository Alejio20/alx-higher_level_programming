#!/usr/bin/python3

def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    res = 0
    i = 0

    while (i < len(roman_string)):
        # Getting value of symbol s[i]
        s1 = roman[roman_string[i]]
        if (i + 1 < len(roman_string)):
            # Getting value of symbol s[i + 1]
            s2 = roman[roman_string[i + 1]]
            # Comparing both values
            if (s1 >= s2):
                # Value of current symbol is greater or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
                # Value of current symbol is greater or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res
