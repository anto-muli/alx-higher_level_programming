#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Stops the user from instantiating new LockedClass attributes
    for everything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
