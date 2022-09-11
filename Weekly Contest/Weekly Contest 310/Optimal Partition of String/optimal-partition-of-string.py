class Solution:
    def partitionString(self, s: str) -> int:
        
        res = 0        
        ss = ""
        
        for i in range(len(s)):
            c = s[i]
            if c in ss:
                ss = c
                res += 1
            else:
                ss += c
        
        if len(ss) > 0:
            res += 1
        return res
