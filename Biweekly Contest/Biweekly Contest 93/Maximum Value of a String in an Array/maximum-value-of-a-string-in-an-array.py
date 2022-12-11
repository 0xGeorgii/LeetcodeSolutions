class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        res = -inf
        lc = set(string.ascii_lowercase)
        
        for s in strs:
            if len(list(lc & set(s))) > 0:
                res = max(res, len(s))
            else:
                res = max(res, int(s))

        return res
