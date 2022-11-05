from typing import List


class Solution:
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

    
def main():
    solution = Solution()
    res = solution.maximumScore([-5,-3,-3,-2,7,1],[-10,-5,3,4,6])
    print(res)

if __name__ == "__main__":
    main()
