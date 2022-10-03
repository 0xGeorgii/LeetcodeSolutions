class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        data = list(zip(neededTime, colors))
        res = 0
        segment = []
        
        def calc_segment():
            _sum = 0
            segment.sort()
            for s in segment[:-1]:
                _sum += s[0]
            return _sum
        
        for i in range(len(data) - 1):
            
            if len(segment) > 0 and data[i][1] != data[i+1][1]:
                segment.append(data[i])
                res += calc_segment()
                segment = []
            
            if data[i][1] == data[i+1][1]:
                segment.append(data[i])
                
                if i+1 >= len(data) - 1:
                    segment.append(data[i+1])
                    res += calc_segment()
        
        return res
