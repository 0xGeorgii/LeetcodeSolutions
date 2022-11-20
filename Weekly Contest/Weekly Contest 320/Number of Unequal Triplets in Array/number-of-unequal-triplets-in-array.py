class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ln = len(nums)
        res = 0
        
        for i in range(ln):
            for j in range(i, ln):
                for k in range(j, ln):
                    t = (nums[i], nums[j], nums[k])
                    if len(t) == len(set(t)):
                        res += 1

        return res
