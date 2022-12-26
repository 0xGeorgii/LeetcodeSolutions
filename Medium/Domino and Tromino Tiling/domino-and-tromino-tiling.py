class Solution:
    def numTilings(self, n: int) -> int:
        
        if n in [1, 2]: return n
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5

        for i in range(3, n):
            dp[i] = dp[i-1] * 2 + dp[i-3]
        
        return dp[n - 1] % int(1e9 + 7)
