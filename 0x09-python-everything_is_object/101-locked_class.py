#!/usr/bin/python3
# 101-locked_class.py
"""

This is a module that containts a clas that avoids
dynmaically created attributes

"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
