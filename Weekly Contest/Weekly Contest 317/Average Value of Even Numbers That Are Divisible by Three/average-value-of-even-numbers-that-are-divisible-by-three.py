class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        res = []
        
        for n in nums:
            
            if n % 2 == 0 and n % 3 == 0:
                res.append(n)
                
        if len(res) == 0:
            return 0
        
        return int(mean(res))
