class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        projects = list(zip(capital, profits))
        projects.sort(key=lambda x: (x[0], -x[1]))
        projects = deque(projects)

        n = 0
        tmp = []

        for _ in range(len(profits)):
            if n == k: break
            while projects and projects[0][0] <= w:
                heapq.heappush(tmp, -projects.popleft()[1])
            
            if tmp:
                w += -heapq.heappop(tmp)
                n += 1
        
        while tmp and n < k:
            w += -heapq.heappop(tmp)
            n += 1

        return w
