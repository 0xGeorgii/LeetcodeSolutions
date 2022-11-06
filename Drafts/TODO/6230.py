from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        ln = len(nums)
        
        dp = [ [0] * ln for _ in range(ln) ]
        res = 0
        
        for i in range(ln):
            for j in range(i, ln):
                
                if i == j:
                    dp[i][j] = nums[i]
                else:    
                    if nums[j] not in dp[i]:
                        dp[i][j] = nums[j]
                    else:
                        break

                if j+1-i == k:
                    res = max(res, sum(dp[i]))
                    break
        
        return res


def main():

    cases = [
        [
            [1,1,1,1,1,1],
            1
        ]
    ]

    s = Solution()
    for case in cases:
        r = s.maximumSubarraySum(case[0], case[1])
        print(r)

if __name__ == "__main__":
    main()