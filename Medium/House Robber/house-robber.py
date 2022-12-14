class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]
        elif len(nums) == 2: return max(nums[0], nums[1])

        ln = len(nums)
        res = -inf

        for i in range(ln):
            dp = [0] * ln
            for j in range(i, ln):
                dp[j] = max(dp[j-2] + nums[j], dp[j-1])

            res = max(res, dp[-1])
        
        return res
