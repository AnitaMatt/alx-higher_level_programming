#!/usr/bin/python3
"""This is a Singly Linked List"""


class Node:
    """Defining a node"""
    def __init__(self, data, next_node=None):
        """Initializing node with data"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """setting the data value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """setting the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setting the next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list"""
    def __init__(self):
        """initializing head"""
        self.__head = None

    def sorted_insert(self, value):
        """public method"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                   temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """printing a singly linked list"""
        content = []
        temp = self.__head
        while temp is not None:
            content.append(str(temp.data))
            temp = temp.next_node
        return ("\n".join(content))
