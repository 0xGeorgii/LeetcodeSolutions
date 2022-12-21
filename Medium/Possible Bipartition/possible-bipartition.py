class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        m = [0] * n
        blank = 0
        blue = 10e3
        red = -10e3
        graph = defaultdict(list)

        for d in dislikes:
            graph[d[0] - 1].append(d[1] - 1)
            graph[d[1] - 1].append(d[0] - 1)

        def dfs(vertex, color):
            m[vertex] = color
            for v in graph[vertex]:
                if m[v] == color: return False
                if m[v] == blank and not dfs(v, -color):
                    return False
            return True

        
        for i in range(n):
            if m[i] == blank and not dfs(i, blue):
                return False

        return True
