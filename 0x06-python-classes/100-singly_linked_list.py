#!/usr/bin/python3
"""Creating a node for our single linked list.
"""


class Node:
    """This class contains attributes for the node.
    """
    def __init__(self, data, next_node=None):
        """Initializing the object.
        Args:
            data: data for the node
            next_node: node to point to
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieving data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """putting restrictions on the data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """retrieving next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """restrictions on next node.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


"""creating single_linked_list.
"""


class SinglyLinkedList:
    """single linked list.
    """
    def __init__(self):
        """initialization.
        """
        self.__head = None

    def sorted_insert(self, value):
        """inserts node at correct position.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while temp.next_node is not None and temp.next_node.data < value:
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """defining how our list should be printed.
        """
        r = ""
        tmp = self.__head
        while tmp is not None:
            if tmp.next_node is None:
                r += str(tmp.data)
            else:
                r += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return r
