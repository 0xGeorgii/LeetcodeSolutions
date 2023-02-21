class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (left+right) // 2
            x = nums[m]
            
            if m % 2 == 0:
                if m < len(nums) - 1 and nums[m+1] == x:
                    left = m + 1
                else:
                    right = m - 1
            else:
                if m < len(nums) - 1 and nums[m+1] == x:
                    right = m - 1
                else:
                    left = m + 1

        return nums[left]
