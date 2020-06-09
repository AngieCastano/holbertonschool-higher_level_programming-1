#!/usr/bin/python3

def printif0(num):
    try:
        if not isinstance(num, int):
            raise TypeError
        if isinstance(num, str):
            raise IndexError
        if num == 0:
            print("{:d}".format(num))
        else:
            print("is not 0")
    except TypeError:
        print("num must be an integer")
    except:
        print("not a type error")

if __name__ == "__main__":
    printif0(0)
    printif0(1)
    printif0("a")
