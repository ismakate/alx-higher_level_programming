#!/usr/bin/python3
# Author - Itai Samuel Makate

def islower(c):
    """Function checks for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
