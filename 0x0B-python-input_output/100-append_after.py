#!/usr/bin/python3
"""append_after function definition"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""

    msg = ""
    with open(filename, mode="r", encoding="utf-8") as read_file:
        for line in read_file:
            msg += line
            if search_string in line:
                msg += new_string

    with open(filename, mode="w", encoding="utf-8") as write_file:
        write_file.write(msg)
