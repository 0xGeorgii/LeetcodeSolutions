class Allocator:

    def __init__(self, n: int):
        self.data = [0] * n
        self.map = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        
        si = 0
        while True:
            try:                
                start_i = self.data.index(0, si)
                if start_i + size > len(self.data):
                    return -1
                for i in range(start_i, start_i + size):
                    if self.data[i] != 0:
                        si = i
                        break
                else:
                    for i in range(start_i, start_i + size):
                        self.data[i] = mID
                    self.map[mID].append([start_i, size])
                    return start_i
            except ValueError:
                return -1

    def free(self, mID: int) -> int:
        res = 0
        for m in self.map[mID]:
            index = m[0]
            ml = m[1]
            res += ml
            for i in range(index, index+ml):
                self.data[i] = 0
        del self.map[mID]
        
        return res
