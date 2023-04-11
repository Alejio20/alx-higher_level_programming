#!/usr/bin/python3
"""MyList module definition"""


class MyList(list):
    """MyList class inherits list"""
    def print_sorted(self):
        """Prints the sorted list (ascending sort)"""
        print(sorted(self))
