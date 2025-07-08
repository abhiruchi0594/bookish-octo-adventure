"""It is collection of nodes where each node contains a data field and two pointers, one pointing to the next node and another pointing to the previous node.
A doubly linked list allows traversal in both directions, forward and backward, making it more flexible than a singly linked list. Each node in a doubly linked list contains three fields: a pointer to the previous node, a pointer to the next node, and the data itself.
A doubly linked list is a data structure that consists of a sequence of nodes, where each node contains a reference to both the next and previous nodes in the sequence. This allows for efficient insertion and deletion of nodes at both ends of the list, as well as traversal in both directions.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    pass