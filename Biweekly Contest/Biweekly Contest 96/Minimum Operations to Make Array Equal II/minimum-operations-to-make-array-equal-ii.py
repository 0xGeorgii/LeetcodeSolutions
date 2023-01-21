class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        neg, pos = 0, 0
        if k == 0:
            return 0 if nums1 == nums2 else -1
        
        for i in range(len(nums1)):
            
            n = nums1[i] - nums2[i]
            if n == 0:
                continue
            
            if n % k != 0:
                return -1
            
            if n > 0:
                pos += n
            else:
                neg += n
        
         
        if -neg != pos: return -1
        
        pos = pos // k
        
        return pos
