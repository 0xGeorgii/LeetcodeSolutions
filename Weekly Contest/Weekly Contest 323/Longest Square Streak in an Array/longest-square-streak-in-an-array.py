class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        res = -1
        data = set(nums)
                
        for n in data:
            rs = 1
            x = n
            while True:
                if x**2 in data:
                    x = x**2
                    rs += 1
                else:
                    break

            res = max(res, rs)
        
        return res if res > 1 else -1
