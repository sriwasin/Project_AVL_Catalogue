class Queue:
    """
    This is a basic queue that will be used to support operation of BST/AVL tree
    """

    def __init__(self):
        self._data = []

    def enqueue(self, value: object) -> None:
        self._data.append(value)

    def dequeue(self):
        return self._data.pop(0)

    def is_empty(self) -> bool:
        return len(self._data) == 0


class Stack:
    """
    This is a basic stack that will be used to support operation of BST/AVL tree
    """

    def __init__(self):
        self._data = []

    def push(self, value: object) -> None:
        self._data.append(value)

    def pop(self):
        return self._data.pop()

    def top(self):
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0


