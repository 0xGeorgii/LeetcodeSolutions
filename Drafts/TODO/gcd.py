import math
from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
                
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

def main():

    cases = [
        [
            [3,12,9,6], 3
        ]
    ]

    for case in cases:
        s = Solution()
        print(s.subarrayGCD(case[0], case[1]))

if __name__ == "__main__":
    main()
