class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        data = {}

        for i, n in enumerate(nums):
            data[n] = i

        for i, n in enumerate(nums):          
            d = target - n

            if d in data and data[d] != i:
                return [ i, data[d] ]
