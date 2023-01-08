class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        res = 0        
        arr = []
        
        for n in nums:
            heapq.heappush(arr, -n)
            
        for i in range(k):
            n = heapq.heappop(arr)
            res += -n
            n = n // 3
            heapq.heappush(arr, n)

        return res
