class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        res, acc = 0, 0
        data = [0] * k
        data[0] = 1

        for n in nums:
            acc = abs(acc + (n % k)) % k
            res += data[acc]
            data[acc] += 1

        return res
