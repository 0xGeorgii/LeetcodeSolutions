class Solution:
    def alternateDigitSum(self, n: int) -> int:
        
        s = str(n)
        res = 0
        
        for i in range(len(s)):
            res += int(s[i]) if i % 2 == 0 else -int(s[i])
        
        return res
