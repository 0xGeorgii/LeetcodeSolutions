class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        res = []
        evens = set()
        s = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.add(i)
                s += nums[i]

        for i in range(len(queries)):
            ni = queries[i][1]
            
            was_even = ni in evens
            n = nums[ni]
            if was_even:
                s -= n
                evens.remove(ni)
                
            nums[ni] = n + queries[i][0]
            
            if nums[ni] % 2 == 0:
                s += nums[ni]
                evens.add(ni)
                
            res.append(s)
            
        return res
