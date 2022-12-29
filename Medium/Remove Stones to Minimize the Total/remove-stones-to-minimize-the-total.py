class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        
        for pile in piles:
            heapq.heappush(heap, -pile)
        
        for _ in range(k):
            n = heapq.heappop(heap)
            n = math.floor(n / 2)
            heapq.heappush(heap, n)
        
        return -sum(heap)
