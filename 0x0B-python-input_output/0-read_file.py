#!/usr/bin/python3
"""read_file function definition"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(filename, mode="r", encoding="utf-8") as files:
        for line in files:
            print(line)
