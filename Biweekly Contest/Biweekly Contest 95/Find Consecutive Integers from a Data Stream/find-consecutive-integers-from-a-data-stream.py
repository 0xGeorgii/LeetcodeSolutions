class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.val = value
        self.data = []
        self.tail_len = 0
        self.is_seq = False

    def consec(self, num: int) -> bool:
        self.data.append(num)
        if num == self.val:
            self.is_seq = True
            self.tail_len += 1
        else:
            self.is_seq = False
            self.tail_len = 0
        
        return self.is_seq and self.tail_len >= self.k

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
