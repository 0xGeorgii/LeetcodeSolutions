class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        s = set()
        
        for i in range(1, len(nums)):
            n = nums[i-1] + nums[i]
            if n in s: return True
            s.add(n)
        
        return False
