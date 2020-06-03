#!/usr/bin/python3
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

'''
I/O Python
Adds all arguments to a Python list,
and then save them to a file
'''


try:
    new_list = load_from_json_file('add_item.json')
except Exception:
    new_list = list()
finally:
    for i in range(1, len(sys.argv)):
        new_list.append(sys.argv[i])
    save_to_json_file(new_list, 'add_item.json')
