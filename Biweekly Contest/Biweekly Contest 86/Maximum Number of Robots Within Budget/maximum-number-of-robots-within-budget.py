from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        
        d = zip(chargeTimes, runningCosts)
        
        q = deque([])
        mp, acc = SortedList(), 0
        res = 0
        
        for t, c in d:
            mp.add(t)
            m = mp[-1]
            acc += c
            q.append((t, c))
            k = len(q)
            
            b = m + k * acc
            
            if b <= budget:
                res = max(res, k)
            else:
                while q and b > budget:
                    t, c = q.popleft()
                    mp.remove(t)
                    m = mp[-1] if len(mp) > 0 else 0
                    acc -= c
                    k = len(q)
                    b = m + k * acc
                
                if len(q) == 0:
                    m = []
                    acc = 0

        return res
