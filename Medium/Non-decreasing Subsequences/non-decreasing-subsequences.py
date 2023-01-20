class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        res = set()

        def find_ss(array, index):
            if array[-1] <= nums[index]:
                a = array + [ nums[index]]
                res.add(tuple(a))
                if index + 1 < len(nums):
                    find_ss(a[:], index + 1)
            if index + 1 < len(nums):
                find_ss(array[:], index + 1)

        for i in range(len(nums)-1):
            find_ss([nums[i]], i+1)

        return res
