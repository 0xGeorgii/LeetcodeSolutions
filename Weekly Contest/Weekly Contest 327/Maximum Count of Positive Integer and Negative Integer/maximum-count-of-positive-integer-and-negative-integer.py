class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        np, nn = 0, 0
        
        for n in nums:
            
            if n > 0:
                np += 1
            elif n < 0:
                nn += 1
        
        return max(np, nn)
