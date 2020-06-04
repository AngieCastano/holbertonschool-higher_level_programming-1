#!/usr/bin/python3
'''
I/O Python
Adds all arguments to a Python list,
and then save them to a file
'''

from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


try:
    new_list = load_from_json_file('add_item.json')
except Exception:
    new_list = list()
finally:
    for i in argv[1:]:
        new_list.append(i)
    save_to_json_file(new_list, 'add_item.json')
