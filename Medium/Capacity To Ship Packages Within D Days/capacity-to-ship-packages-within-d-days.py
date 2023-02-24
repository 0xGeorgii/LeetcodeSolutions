class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        lw = len(weights)
        if days == lw: return max(weights)

        def check_capacity(c):
            res = 1
            acc = 0
            for w in weights:
                acc += w
                if acc > c:
                    res += 1
                    if res > days: return False
                    acc = w

            return True

        left = max(weights)
        right = 500 * 5 * 10000

        while left < right:
            m = (left+right) // 2
            if check_capacity(m):
                right = m
            else:
                left = m + 1

        return left
