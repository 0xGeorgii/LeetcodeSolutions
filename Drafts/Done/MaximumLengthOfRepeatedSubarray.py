from typing import List

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        dp = [ [0] * (n2) for _ in range(n1) ]
        
        for i in range(n1):
            for j in range(n2):
                if i == 0 or j == 0:
                    dp[i][j] = 1 if nums1[i] == nums2[j] else 0
                else:
                    dp[i][j] = 1 + dp[i-1][j-1] if nums1[i] == nums2[j] else 0
            
            
        return max(max(x) for x in dp)

def main():
    solution = Solution()
    cases = [
        [ [1,2,3,2,1],[3,2,1,4,7] ],
        [ [0,0,0,0,0], [0,0,0,0,0] ],
        [ [0,0,0,0,1], [1,0,0,0,0] ],
        [ [1,2,3,2,1], [3,2,1,4] ]
    ]
    for case in cases:
        res = solution.findLength(case[0], case[1])
        print(res)

if __name__ == "__main__":
    main()
