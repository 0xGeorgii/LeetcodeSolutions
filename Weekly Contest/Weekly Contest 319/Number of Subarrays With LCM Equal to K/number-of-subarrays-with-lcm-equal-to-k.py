class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(nums)):
            l = 1
            for j in range(i, len(nums)):
                l = math.lcm(nums[j], l)
                if l == k:
                    res += 1
                    
        return res
