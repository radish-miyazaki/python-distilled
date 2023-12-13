class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self):
        return f"<{type(self).__name__} at 0x{id(self):x}, size={len(self._items)}>"

    def __len__(self):
        return len(self._items)


class MyStack(Stack):
    def swap(self):
        a = self.pop()
        b = self.pop()
        self.push(a)
        self.push(b)


class NumericStack(Stack):
    def push(self, item):
        if not isinstance(item, (int, float)):
            raise TypeError("Expected an int or float")
        super().push(item)


class Calculator:
    def __init__(self):
        self._stack = Stack()

    def push(self, item):
        self._stack.push(item)

    def pop(self):
        return self._stack.pop()

    def add(self):
        self.push(self.pop() + self.pop())

    def mul(self):
        self.push(self.pop() * self.pop())
