class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        acc = 0

        for n in nums:
            acc = max(0, acc) + n
            res = max(res, acc)
        
        return res
