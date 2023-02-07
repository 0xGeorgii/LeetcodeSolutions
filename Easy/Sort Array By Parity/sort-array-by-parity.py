class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = deque([])

        for n in nums:
            if n % 2 == 0:
                res.appendleft(n)
            else:
                res.append(n)

        return res
