"""Linked list is a data structure that consists of nodes, where each node contains data and a reference to the next_node_ref node in the sequence.
It allows for efficient insertion and deletion of elements, as well as dynamic memory allocation.
Linked lists can be singly linked (each node points to the next_node_ref node) or doubly linked (each node points to both the next_node_ref and previous nodes).
They are often used in scenarios where the size of the data structure is not known in advance or when frequent insertions and deletions are required.


Node: Element of a linked list that contains data and a reference to the next_node_ref node.
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

1. Singly linked list: Each node points to the next_node_ref node, forming a unidirectional chain.
2. Doubly linked list: Each node points to both the next_node_ref and previous nodes, allowing for bidirectional traversal.
3. Circular linked list: The last node points back to the first node, creating a circular structure."""


# Define a Node which stores data and a reference to the next_node_ref node
class Node:
    def __init__(self, data):
        self.data = data            # Holds the value
        self.next_node_ref = None            # Points to the next_node_ref node (initially None)


# Define the LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None  # Head points to the first node of the list

    # Function to traverse the list and print data + memory references
    def traverse(self):
        print("\n🔁 Traversing Linked List:")
        current = self.head
        while current:
            print(
                f"[Data: {current.data} | NextRef: {id(current.next_node_ref) if current.next_node_ref else None}] -> ",
                end=""
            )
            current = current.next_node_ref
        print("None")

    # Function to add node at the beginning of the list
    def add_at_beginning(self, data):
        print(f"\n➕ Adding {data} at the BEGINNING")
        new_node = Node(data)       # Step 1: Create a new node
        new_node.next_node_ref = self.head   # Step 2: Point new node's next_node_ref to current head
        self.head = new_node        # Step 3: Update head to point to new node

    # Function to add node at the end of the list
    def add_at_end(self, data):
        print(f"\n➕ Adding {data} at the END")
        new_node = Node(data)       # Step 1: Create a new node

        if self.head is None:       # If list is empty
            self.head = new_node    # Set head to new node
        else:
            current = self.head
            while current.next_node_ref:     # Traverse to the last node
                current = current.next_node_ref
            current.next_node_ref = new_node # Step 2: Link last node to new node

    # Function to add node at a specific position (0-based index)
    def add_at_position(self, position, data):
        print(f"\n➕ Adding {data} at POSITION {position}")
        if position < 0:
            print("❌ Invalid position: Must be >= 0")
            return

        new_node = Node(data)

        if position == 0:
            self.add_at_beginning(data)
            return

        current = self.head
        count = 0

        # Traverse to the node before the desired position
        while current and count < position - 1:
            current = current.next_node_ref
            count += 1

        if current is None:
            print("❌ Position out of bounds")
        else:
            new_node.next_node_ref = current.next_node_ref
            current.next_node_ref = new_node


# Create LinkedList object
ll = LinkedList()

# Add nodes at various positions
ll.add_at_end(10)
ll.add_at_end(20)
ll.add_at_end(30)

ll.traverse()  # Show list after adding at end

ll.add_at_beginning(5)
ll.traverse()  # Show list after adding at beginning

ll.add_at_position(2, 15)  # Insert 15 at index 2 (between 10 and 20)
ll.traverse()  # Show final list with all updates