class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        maxp = 0
        
        arr = sorted(nums, reverse=True)
        
        for i in range(len(nums)-2):
            a = arr[0 + i]
            b = arr[1 + i]
            c = arr[2 + i]

            if a + c <= b or b + c <= a or a + b <= c:
                continue
            else:
                maxp = max(maxp, sum([a,b,c]))
                break
        
        return maxp
