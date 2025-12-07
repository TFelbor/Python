
# A class for stacks
class Stack(object):

    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def clear(self):
        self.stack = []

    def is_empty(self):
        return not self.stack

    def __str__(self):
        if self.is_empty():
            print("Stack is empty")
        return "Stack contents: " + str(self.stack)

