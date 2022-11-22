class Data:
    perfect_squares = []

    def __init__(self):
        if len(self.perfect_squares) == 0:
            x = 1
            while x < 10e4:                
                self.perfect_squares.append(x)
                x = (1 + isqrt(x)) ** 2
            self.perfect_squares.sort()

class Solution:

    def numSquares(self, n: int) -> int:
        data = Data()

        if n in data.perfect_squares:
            return 1
       
        ps = [ p for p in data.perfect_squares if p < n]

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, len(dp)):
            for j in ps:
                if j <= i:
                    dp[i] = min(dp[i], 1 + dp[i-j])

        return dp[-1]
