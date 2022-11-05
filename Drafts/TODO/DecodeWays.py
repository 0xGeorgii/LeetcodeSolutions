class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == "0":
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(s)+1):
            opts = 0

            if s[i-1] == "0":
                #dp[i] = dp[i-1]
                opts = -1

            if i >= 2:
                n = int(s[i-2:i]) - 1
                if 10 <= n < 26:
                    opts += 1

            dp[i] = dp[i-1] + opts

        return dp[-1]

def main():
    solution = Solution()
    cases = [
        # [ "12", 2 ],
        # [ "226", 3 ],
        # [ "06", 0 ],
        [ "10", 1 ],
        [ "27", 1 ],
        [ "2101", 1 ]
    ]
    for case in cases:
        res = solution.numDecodings(case[0])
        print(f"out: {res} exp: {case[1]} -> {res == case[1]}")


if __name__ == "__main__":
    main()
