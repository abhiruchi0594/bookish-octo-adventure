from collections import deque
from queue import LifoQueue

class StackUsingDeque:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("pop from an empty stack")
        return self.items.pop()


class StackUsingLifoQueue:
    def __init__(self):
        self.items = LifoQueue()

    def is_empty(self):
        return self.items.empty()

    def push(self, item):
        self.items.put(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.get()



# Example usage

if __name__ == "__main__":
    stack_deque = StackUsingDeque()
    stack_deque.push(1)
    stack_deque.push(2)
    print(stack_deque.items)
    print(stack_deque.pop())  # Output: 2
    # print(stack_deque.pop())  # Output: 1

    stack_lifo = StackUsingLifoQueue()
    stack_lifo.push('a')
    stack_lifo.push('b')
    # print(stack_lifo.pop())  # Output: 'b'
    # print(stack_lifo.pop())  # Output: 'a'

