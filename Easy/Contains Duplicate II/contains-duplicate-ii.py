class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        data = defaultdict()
        
        for i, n in enumerate(nums):
            
            if n in data and i - data[n] <= k:
                return True
            else:
                data[n] = i
            
        return False
