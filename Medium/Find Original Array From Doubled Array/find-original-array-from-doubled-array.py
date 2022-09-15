class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) == 1 or len(changed) % 2 != 0:
            return []

        data = defaultdict(int)
        for i in range(len(changed)):
            data[changed[i]] += 1
        
        res = []

        for k in sorted(data.keys()):
            if data[k] == 0:
                continue

            for i in range(data[k]):
                if data[k] == 0:
                    break
                if k * 2 in data and data[k * 2] > 0:
                    data[k] -= 1
                    data[k * 2] -= 1
                    res.append(k)
                else:
                    return []
                
            if data[k] > 0:
                return []
            
        return res

