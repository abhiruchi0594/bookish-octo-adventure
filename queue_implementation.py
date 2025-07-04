"""queue is the linear data structure where element is inserted from one end and removed from the other end, hence it is open at the front and rear end.
The end where elements are added is called the rear/back/tail and the end where elements are removed is called the front/head of the que.
It follows the First In First Out (FIFO) principle, meaning the first element added to the queue will be the first one to be removed. or we can say
LILO (Last In Last Out) principle, meaning the last element added to the queue will be the last one to be removed.

The process of adding an element to the queue is called enqueue, and the process of removing an element from the queue is called dequeue."""


class QueueWithList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)


from collections import deque


class QueueWithDeque:

    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        return self.items.popleft()



deque_object = QueueWithDeque()
# Example usage
if __name__ == "__main__":
    queue_list = QueueWithList()
    queue_list.enqueue(1)
    queue_list.enqueue(2)
    print(queue_list.items)  # Output: [1, 2]
    queue_list.dequeue()
    print(queue_list.items)  # Output: [2]

    queue_deque = QueueWithDeque()
    queue_deque.enqueue('a')
    queue_deque.enqueue('b')
    print(queue_deque.items)  # Output: deque(['a', 'b'])
    print(queue_deque.dequeue())  # Output: 'a'
    print(queue_deque.items)  # Output: deque(['b'])

import queue

q = queue.Queue()
q.put(1)
q.put(2)
q.get()  # Output: 1

"""In the Priority Queue, elements are removed based on their priority rather than the order they were added.
priority could be defined by a number, where lower numbers have higher priority. or it could be a tuple where the first element is the priority and the second element is the value."""

q = queue.PriorityQueue()
q.put(10)
q.put(5)
q.put(20)
print(q.get())  # Output: 5
print(q.get())  # Output: 10



