class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        res = list(nums)
        
        for n in nums:
            s = str(n)[::-1]
            if s[0] == "0":
                s = s[1:]
            res.append(int(s))
            
        res = set(res)
        return len(res)
