class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        heap = []
        
        for g in gifts:
            heapq.heappush(heap, -g)
                
        for i in range(k):
            n = -heapq.heappop(heap)
            n = int(math.sqrt(n))
            heapq.heappush(heap, -n)
        
        
        return -sum(heap)
