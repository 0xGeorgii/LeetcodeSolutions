class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        queue = deque([(start, 0)])
        visited = set(start)
        
        while len(queue) > 0:
            
            w, i = queue.popleft()
            
            if w == end:
                return i
            
            for ch in "ACGT":
                for j in range(8):
                    nw = w[:j] + ch + w[j+1:]
                    
                    if nw in bank and nw not in visited:
                        queue.append((nw, i + 1))
                        visited.add(nw)
        
        return -1
