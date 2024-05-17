#!/usr/bin/python3
"""
    Write a class Node that defines a node of a singly linked list by:

    Private instance attribute: data:
        property def data(self): to retrieve it
        property setter def data(self, value): to set it:
            data must be an integer, otherwise raise a TypeError exception with the message data must be an integer
    Private instance attribute: next_node:
        property def next_node(self): to retrieve it
        property setter def next_node(self, value): to set it:
            next_node can be None or must be a Node, otherwise raise a TypeError exception with the message next_node must be a Node object
    Instantiation with data and next_node: def __init__(self, data, next_node=None):

And, write a class SinglyLinkedList that defines a singly linked list by:

    Private instance attribute: head (no setter or getter)
    Simple instantiation: def __init__(self):
    Should be printable:
        print the entire list in stdout
        one node number by line
    Public instance method: def sorted_insert(self, value): that inserts a new Node into the correct sorted position in the list (increasing order)
    You are not allowed to import any module

"""
class Node():
    def _init_(self, data, next_node=None):
        self._data = data
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        if type(data) is not int:
            raise TypeError("data must be an integer")

        self._next_node = next_node
    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        self._next_node = value
        if next_node is None or None:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList():
    def _init_(self):
        self._head = head

    def sorted_insert(self, value):
        self.new_node = value
