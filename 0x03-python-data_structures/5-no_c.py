#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    for i in my_string:
        if i != "c" and i != "C":
            new_list.append(i)
    separator = ""
    new_string = separator.join(new_list)
    return new_string
