class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        banned = set(banned)
        res =  0
        acc = 0
        
        for i in range(1, n + 1):
            if i in banned:
                continue
            if acc + i <= maxSum:
                acc += i
                res += 1
        
        return res
