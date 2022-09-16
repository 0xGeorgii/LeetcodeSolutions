class Solution:
    
    #2D array approach
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
                m = len(multipliers)
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for mi in range(m - 1, -1, -1):
            for ni in range(mi, -1, -1):

                l = multipliers[mi] * nums[ni] + dp[mi + 1][ni + 1]
                r = multipliers[mi] * nums[n - 1 - (mi - ni)] + dp[mi + 1][ni]

                dp[mi][ni] = max(l, r)

        return dp[0][0]
    
    #recursive approach
    def _maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        data = {}
        
        ml = len(multipliers)
        nl = len(nums)
        
        def calcVariants(ni, mi):
            if mi >= ml:
                return 0
            
            if (ni, mi) in data:
                return data[(ni, mi)]

            l = nums[ni] * multipliers[mi] + calcVariants(ni + 1, mi + 1)
            r = nums[(nl-1)-(mi-ni)] * multipliers[mi] + calcVariants(ni, mi + 1)

            res = max(l,r)
            data[(ni, mi)] = res
            return res
    
        return calcVariants(0, 0)

