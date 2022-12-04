# 💡Python O(n) simple solution

# Intuition
According to constraint `1 <= nums.length <= 10 ** 5` we cannot re-calculate avg values for sub-arrays every time.

# Approach

1. Right handside area
   1. Calculate a sum for all elements in `nums` for the further tracking
   2. Remember `nums` len
2. Left handside area
   1. Set placeholders because we begin with the first index `0` we have nothing on the left area so it is `0` as well as the count of elements is `0`
3. On each step of iteration we need to transfer numbers from the right area to the left area. We can do it by substituion the current number from the right area sum and adding it to the left area. Also we update the numbers of integers accordingly.

# Complexity
- Time complexity: O(n)
- Space complexity: O(1)

# Code
```
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        sum_right = sum(nums)
        len_right = len(nums)
        sum_left = 0
        len_left = 0

        min_avg = inf
        index = 0

        for i in range(len(nums)):
            
            sum_left += nums[i]
            len_left += 1

            sum_right -= nums[i]
            len_right -= 1

            #in case of only zeroes left on right
            if sum_right == 0:
                v = sum_left // len_left
            else:
                v = abs(
                    sum_left // len_left - sum_right // len_right
                )

            if v < min_avg:
                min_avg = v
                index = i

        return index

```
