class TimeMap:

    def __init__(self):
        self.data = []

    def set(self, key: str, value: str, timestamp: int) -> None:        
        self.data.append((timestamp, key, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        for i in range(len(self.data) - 1, -1, -1):
            item = self.data[i]
            if item[0] > timestamp:
                continue
            if item[1] == key:
                return item[2]
        
        return ""
