class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = defaultdict(str)
        
        for i in range(len(names)):
            data[heights[i]] = names[i]
            
        res = []
        
        for k in sorted(data.keys(), reverse=True):
            res.append(data[k])
            
        return res
