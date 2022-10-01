class Solution:
    def equalFrequency(self, word: str) -> bool:
        data = [0] * 26
        
        for c in word:
            data[ord(c) - ord('a')] += 1
            
        data = list(filter(lambda x: x != 0, data))

        for i in range(len(data)):
            d = list(data)
            d[i] -= 1
            if d[i] == 0:
                del d[i]
            if len(set(d)) <= 1:
                return True

        return False
