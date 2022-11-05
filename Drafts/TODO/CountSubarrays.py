from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
        ln = len(nums)
        
        dp = [ [0] * (ln) for _ in range(ln) ]
        
        for i in range(ln):
            for j in range(i, ln):
                if j == i and nums[j] != minK:
                    break
                elif j + 1 >= ln and nums[j] != maxK:
                    dp[i] = [-1]
                    break
                else:
                    if nums[j] == maxK and (j+1 < ln and nums[j+1] != maxK):
                        dp[i][j] = -1
                        break
                    else:
                        dp[i][j] = 1 + dp[i][j-1]
            
            
        return sum(max(x) for x in dp)

def main():
    cases = [
        [
            [1,3,5,2,7,5],
            1,
            5
        ],
        [
            [1,1,1,1],
            1,
            1
        ],
        [
            [1,2,3,4,5,4,4,1,2,3,4],
            1,
            5
        ]
    ]

    s = Solution()

    for case in cases[2:]:
        print(s.countSubarrays(case[0], case[1], case[2]))

if __name__ == "__main__":
    main()
