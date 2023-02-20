class Solution:
    def searchInsert(self, nums: List[int], t: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            m = (right+left) // 2
            x = nums[m]
            if x == t: return m

            if x < t:
                left = m + 1
            elif x > t:
                right = m - 1
        
        return left
