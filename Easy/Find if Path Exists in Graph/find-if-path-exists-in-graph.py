class Solution:
    def validPath(self, n: int, edges: List[List[int]], src: int, dst: int) -> bool:
        
        if src == dst: return True
        
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        seen = set()
        queue = deque([src])

        while queue:
            tmp = deque([])
            while queue:
                node = queue.popleft()
                for e in graph[node]:
                    if e not in seen:
                        if e == dst: return True
                        seen.add(e)
                        tmp.append(e)
            queue = tmp

        return False
