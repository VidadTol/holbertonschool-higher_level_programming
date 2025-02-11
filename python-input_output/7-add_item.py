#!/usr/bin/python3
"""
This script adds all arguments to a Python list and saves them to a file.
"""

import sys
import os

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

if os.path.exists(filename):
    """
    Check if the file exists. If it does, load the existing list from the file.
    """
    my_list = load_from_json_file(filename)
else:
    """
    If the file does not exist, create an empty list.
    """
    my_list = []
"""
Extend the list with the arguments passed to the script.
"""
my_list.extend(sys.argv[1:])

"""
Save the updated list back to the file.
"""
save_to_json_file(my_list, filename)
