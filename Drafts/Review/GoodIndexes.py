from itertools import groupby
from typing import List
# You are given an integer array nums of size n.

# Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

# In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
# Return the length of the longest such subarray.

# The bitwise AND of an array is the bitwise AND of all the numbers in it.

# A subarray is a contiguous sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,2,3,3,2,2]
# Output: 2
# Explanation:
# The maximum possible bitwise AND of a subarray is 3.
# The longest subarray with that value is [3,3], so we return 2.
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 1
# Explanation:
# The maximum possible bitwise AND of a subarray is 4.
# The longest subarray with that value is [4], so we return 1.
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        bef = [1]*n
        after = [1]*n
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                bef[i] = bef[i-1]+1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                after[i] = after[i+1]+1
 
        res = []
        for i in range(k, n-k):
            if bef[i-1] >= k and after[i+1] >= k:
                res.append(i)
        return res



    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        res = 0
        for x, y in groupby(nums):
            if x == m:
                res = max(res, len(list(y)))
        return res

def main():
    solution = Solution()
    res = solution.goodIndices([440043,276285,336957],1)
    print(res)
    res = solution.goodIndices([2,1,1,2], 2)
    print(res)
    res = solution.goodIndices([2,1,1,1,3,4,1], 2)
    print(res)
    res = solution.goodIndices([388589,17165,726687,401298,600033,537254,301052,151069,399955], 4)
    print(res)

if __name__ == "__main__":
    main()
