"""Linked list is a data structure that consists of nodes, where each node contains data and a reference to the next node in the sequence.
It allows for efficient insertion and deletion of elements, as well as dynamic memory allocation.
Linked lists can be singly linked (each node points to the next node) or doubly linked (each node points to both the next and previous nodes).
They are often used in scenarios where the size of the data structure is not known in advance or when frequent insertions and deletions are required.


Node: Element of a linked list that contains data and a reference to the next node.
starting point: The first node in a linked list, also known as the head.
last node: The last node in a linked list, which points to None (or null) to indicate the end of the list. also known as the tail.

Dynamic memory allocation: The process of allocating memory for data structures at runtime, allowing for flexible and efficient use of memory.
No continuous memory allocation: Linked lists do not require contiguous memory allocation, meaning that nodes can be stored in non-adjacent memory locations.
Advantages of linked lists:
1. Dynamic size: Linked lists can grow or shrink in size as needed, allowing for efficient memory usage.
2. Efficient insertions and deletions: Inserting or deleting nodes in a linked list can be done in constant time, as it only requires updating pointers.
3. No need for resizing: Linked lists do not require resizing like arrays, which can be costly in terms of time and memory.
4. Could be used to implement other data structures: Linked lists can be used to implement stacks, queues, and other data structures, providing flexibility in data organization.
5. Web browsers use linked lists to manage the history of visited pages, allowing for efficient navigation and backtracking.

Disadvantages of linked lists:
1. Memory overhead: Each node in a linked list requires additional memory for storing pointers, which can lead to increased memory usage compared to arrays.
2. Random access is not possible: Linked lists do not allow for direct access to elements by index, making it less efficient for certain operations compared to arrays.

Types of linked lists:

1. Singly linked list: Each node points to the next node, forming a unidirectional chain.
2. Doubly linked list: Each node points to both the next and previous nodes, allowing for bidirectional traversal.
3. Circular linked list: The last node points back to the first node, creating a circular structure."""

