#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file
"""
import sys
import json
from pathlib import Path

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def load_add_save():
    """Adds all arguments to a Python list, and then save them to a file
    """
    path = Path('./add_item.json')
    my_list = []
    if not path.is_file():
        save_to_json_file(my_list, "add_item.json")

    my_list = load_from_json_file("add_item.json")
    list_args = [x for x in sys.argv if x != sys.argv[0]]

    save_to_json_file(my_list + list_args, "add_item.json")


if __name__ == "__main__":
    load_add_save()
