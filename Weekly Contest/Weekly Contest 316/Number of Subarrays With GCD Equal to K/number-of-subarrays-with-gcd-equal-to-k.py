class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            g = nums[i]
            for j in range(i, len(nums)):
                g = math.gcd(g, nums[j])
                if g == k:
                    res += 1
        
        return res

    def _subarrayGCD(self, nums: List[int], k: int) -> int:
                
        res = 0
        start = -1
        
        for i in range(len(nums)):
            if start < 0 and nums[i] % k == 0:
                start = i
                if math.gcd(nums[i]) == k:
                    res += 1
            elif nums[i] % k == 0:
                for j in range(start, i):
                    if math.gcd(*nums[j:i+1]) == k:
                        res += 1
                if math.gcd(nums[i]) == k:
                    res += 1
            else:
                start = -1
        
        return res
