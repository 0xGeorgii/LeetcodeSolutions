class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        res = 1

        p1 = 0

        for i in range(1, len(nums)):
            
            n1 = nums[p1]
            n2 = nums[i]

            if n1 != n2:         
                p1 += 1
                nums[p1] = n2
                res += 1
        
        print(res, nums)
        return res
