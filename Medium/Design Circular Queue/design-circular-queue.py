class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        self.items = []

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.items.insert(0, value)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            del self.items[-1]
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.items[-1]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.items[0]

    def isEmpty(self) -> bool:
        return len(self.items) == 0

    def isFull(self) -> bool:
        return len(self.items) == self.limit
