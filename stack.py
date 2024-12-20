class Stack:
    def __init__(self, stack_=None):
        self.stack = []
        if stack_ is not None:
            self.stack.extend(stack_)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)
