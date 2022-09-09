class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties, key=lambda x: (-x[0],x[1]))
        max_attack = properties[0][0]
        max_defense = properties[0][1]
        
        res = 0
        
        for i in range(1,len(properties)):
            if properties[i][0] < max_attack and properties[i][1] < max_defense:
                res += 1
            else:
                max_attack = properties[i][0]
                max_defense = properties[i][1]
                
                
        return res

# slow solution
class _Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        
        data = defaultdict(list)
        keys = set([])
        
        for i in range(len(properties)):
            bisect.insort(data[properties[i][0]], properties[i][1])
            keys.add(properties[i][0])
            
        keys = sorted(keys)
        keys_len = len(keys)
        res = 0
        
        for k in range(keys_len):
            defs = data[keys[k]]
            for d in defs:
                for i in range(keys_len - 1, k, -1):
                    if d < data[keys[i]][-1]:
                        res += 1
                        break
        return res
