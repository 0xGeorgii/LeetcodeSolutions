class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
                
        ln1 = len(nums1)
        ln2 = len(nums2)
        
        i, j = 0, 0
        
        while True:
            
            if i == ln1 or j == ln2:
                break
            
            n1 = nums1[i]
            n2 = nums2[j]
                        
            if n1 == n2:
                return n1
            
            if n1 < n2:
                i += 1
            else:
                j += 1

        return -1
