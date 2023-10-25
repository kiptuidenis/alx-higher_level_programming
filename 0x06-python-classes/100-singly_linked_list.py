#!/usr/bin/python3
"""This module contains a singly linked list"""


class Node:
    """
    This class represents a node in a singly linked list.

    Attributes:
        data: The data stored in the node.
        next_node: Reference to the next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node with the given data.

        Args:
            data: The data to store in the node.
            next_node: Reference to the next node in
        the list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data field to the given value.

        Args:
            value: The data to set in the node.

        Raises:
            TypeError: If the value is not an integer.
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns:
            The reference to the next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the reference to the next node.

        Args:
            value: Reference to the next node (Node object) or None.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        head: Reference to the first node in the list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts the given value into the list while maintaining sorted order.

        Args:
            value: The value to insert into the list.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return a string representation of the linked list with
        each element on a new line.

        Returns:
            A string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
