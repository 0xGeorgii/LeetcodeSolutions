class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        total = sum(nums)
        r_min = inf
        r_max = -inf

        acc = 0
        for n in nums:
            acc = max(0, acc) + n
            r_max = max(r_max, acc)
        
        acc = 0
        for n in nums:
            acc = min(acc, 0) + n
            r_min = min(r_min, acc)
        
        return r_max if r_min == total else max(r_max, total - r_min)
