class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        
        nums.sort()
        res = set()
        
        for i in range(len(nums) // 2):
            
            n1 = nums[i]
            n2 = nums[-1-i]
            
            res.add(mean([n1, n2]))
        
        return len(res)
