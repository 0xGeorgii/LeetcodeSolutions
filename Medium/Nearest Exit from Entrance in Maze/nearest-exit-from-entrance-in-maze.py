class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque([])
        min_steps = float("inf")
        visited = set()
        steps = 0
        entrance = tuple(entrance)
        queue.append(
            entrance
        )

        while queue:
            tmp = deque([])
            while queue:
                p = queue.popleft()
                if p in visited:
                    continue
                
                visited.add(p)

                if p != entrance:
                    if p[0] == 0 or p[0] == len(maze) - 1:
                        min_steps = min(min_steps, steps)
                        continue
                    
                    if p[1] == 0 or p[1] == len(maze[0]) - 1:
                        min_steps = min(min_steps, steps)
                        continue

                if p[0] - 1 >= 0:
                    m = maze[p[0]-1][p[1]]
                    if m == "." and (p[0]-1, p[1]) not in visited:                        
                        t = (p[0]-1, p[1])
                        tmp.append(t)

                if p[0] + 1 < len(maze):
                    m = maze[p[0]+1][p[1]] 
                    if m == "." and (p[0]+1, p[1]) not in visited:
                        t = (p[0]+1, p[1])
                        tmp.append(t)

                if p[1] - 1 >= 0:
                    m = maze[p[0]][p[1]-1] 
                    if m == "." and (p[0], p[1]-1) not in visited:
                        t = (p[0], p[1]-1)
                        tmp.append(t)

                
                if p[1] + 1 < len(maze[0]):
                    m = maze[p[0]][p[1]+1]
                    if m == "." and (p[0], p[1]+1) not in visited:
                        t = (p[0], p[1]+1)
                        tmp.append(t)

            steps += 1
            queue = tmp

        return min_steps if min_steps < float("inf") else -1
