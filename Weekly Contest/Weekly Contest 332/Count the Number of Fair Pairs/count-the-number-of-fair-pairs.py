class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        nums.sort()        
        res = 0
        
        for x in range(len(nums)-1, -1, -1):
            i1 = bisect_left(nums, lower - nums[x])
            i2 = bisect_right(nums, upper - nums[x]) - 1
            i2 = min(i2, x - 1)
            if i2 >= i1:
                res += (i2 - i1 + 1)
        
        return res
