class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        res = 0 if target > k else 1

        dp = [ [0] * k for _ in range(k+1)]

        for i in range(k):
            dp[0][i] = i + 1
        
        for x in range(n-1):

            for i in range(1, k + 1):
                for j in range(k):
                    r = dp[x][j] + i
                    if r >= target:
                        res += 1
                        break
                    dp[i][j] = r
        
        return res % 7000000000

def main():
    cases = [
        # [ 1, 6, 3, 1],
        # [ 2, 6, 7, 6],
        # [ 3, 6, 7, 15],
        # [ 2, 10, 18, 3],
        [ 30, 30, 500, 222616187]
    ]

    s = Solution()
    for case in cases:
        res = s.numRollsToTarget(case[0], case[1], case[2])
        print(f"out: {res} exp: {case[3]} -> {res == case[3]}")

if __name__ == "__main__":
    main()
