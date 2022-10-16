class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        m = -1
        for i in range(len(nums)):
            n = nums[i]
            if n > 0:
                break
            if abs(n) in nums[i+1:]:
                m = max(m, abs(n))
        
        return m
