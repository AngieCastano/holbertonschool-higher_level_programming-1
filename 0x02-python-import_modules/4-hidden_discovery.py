#!/usr/bin/python3
import hidden_4
list = dir(hidden_4)
for i in (list):
    if i[0] != '_' and i[1] != '_':
        print(i)
