class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        data = defaultdict(int)
        
        for n in nums:
            data[n] += 1
            if data[n] >= 2:
                return n
