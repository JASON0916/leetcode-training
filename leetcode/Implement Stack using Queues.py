"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You may assume that all operations are valid (for example,
no pop or top operations will be called on an empty stack).
Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue -- which means only push to back,
pop from front, size, and is empty operations are valid.
"""
__author__ = 'phoenix'


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)


    # @return nothing
    def pop(self):
        self.queue.pop()

    # @return an integer
    def top(self):
        return self.queue[-1]


    # @return an boolean
    def empty(self):
        return len(self.queue) == 0