#!/usr/bin/python3
islower = __import__('7-islower').islower

print("Alphabet \"g\" is {}" .format(
    "lowercase" if islower("g") else "uppercase"))
print("Alphabet \"R\" is {}".format(
    "lowercase" if islower("R") else "uppercase"))
print("Alphabet \"3\" is {}".format(
    "lowercase" if islower("3") else "uppercase"))
print("Alphabet \"e\" is {}".format(
    "lowercase" if islower("e") else "uppercase"))
print("Alphabet \"N\" is {}".format(
    "lowercase" if islower("N") else "uppercase"))
