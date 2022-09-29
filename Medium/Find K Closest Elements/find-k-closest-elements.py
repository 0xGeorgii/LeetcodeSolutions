class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        heap = []
        
        for i, n in enumerate(arr):
            heapq.heappush(
                heap,
                (abs(n - x), i)
            )
            
        res = []
        
        for i in range(k):
            res.append(arr[heapq.heappop(heap)[1]])
            
        return sorted(res)
