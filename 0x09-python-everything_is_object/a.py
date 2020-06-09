#!/usr/bin/python3
from sys import argv
archivo = open(argv[1] + '-answer.txt', 'w+')
archivo.write(argv[2] + '\n')
archivo.close()
