class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        
        for n in nums:
            for i in str(n):
                res.append(int(i))
        
        return res
