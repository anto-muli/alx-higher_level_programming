#!/usr/bin/python3
"""Writes a script that adds all args to a Python list
& then save them to a file"""
from sys import argv

"""Add all args to a Python list and save them to a file."""

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend(argv[1:])
    save_to_json_file(my_list, "add_item.json")
