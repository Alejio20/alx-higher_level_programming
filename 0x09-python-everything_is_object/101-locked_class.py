#!/usr/bin/python3
"""Locked Class Definition"""


class LockedClass:
    """Prevents dynamic creation of new instance attributes
    except if the new instance attribute is called first_name"""

    __slots__ = ["first_name"]
