#!/usr/bin/python3
"""MyInt inherits from int"""


class MyInt(int):
    """MyInt definition"""

    def __eq__(self, val):
        """Returns == operators inverted to !="""

        return (self.real != val)

    def __ne__(self, val):
        """Returns != operators inverted to =="""

        return (self.real == val)
