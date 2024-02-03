#!/usr/bin/python3
def islower(c):
    if c.isalpha() and ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
