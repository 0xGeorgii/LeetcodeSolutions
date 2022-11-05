from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        nl = len(prices)
        dp = [ [0] * nl for _ in range(nl + 1) ]

        for i, p in enumerate(prices):
            dp[0][i] = p

        offset = 0

        for i in range(nl - 1):
            for j in range(1, nl):
                p = prices[j] - dp[0][i]
                dp[j][i] = p

        return 0

def main():
    cases = [
        [
            [1,2,3,0,2], 3
        ],
        [
            [1], 0
        ]
    ]

    s = Solution()
    for case in cases:
        res = s.maxProfit(case[0])
        print(f"out: {res} exp: {case[1]} -> {res == case[1]}")

if __name__ == "__main__":
    main()
