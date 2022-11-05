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

def main():
    myCircularQueue = MyCircularQueue(3)
    res = myCircularQueue.enQueue(1) # return True
    res = myCircularQueue.enQueue(2) # return True
    res = myCircularQueue.enQueue(3) # return True
    res = myCircularQueue.enQueue(4) # return False
    res = myCircularQueue.Rear()     # return 3
    res = myCircularQueue.isFull()   # return True
    res = myCircularQueue.deQueue()  # return True
    res = myCircularQueue.enQueue(4) # return True
    res = myCircularQueue.Rear()     # return 4


if __name__ == "__main__":
    main()
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
