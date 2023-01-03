class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        res = 0
        all_cells = set()
        start = tuple()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    all_cells.add((i,j))

        queue = deque([
             ( start[0], start[1], set([ start ]) )
            ])
        tmp = deque([])

        def check_and_push(i, j, visited):

            if grid[i][j] in [ 0, 2 ] and (i, j) not in visited:
                # print(visited)
                if grid[i][j] == 2 and len(visited) - 1 == len(all_cells):
                    return True
                elif grid[i][j] == 0:
                    tmp.appendleft((i, j, set([*visited, (i , j)])))
                return False


        while queue:
            tmp = deque([])
            while queue:

                i, j, visited = queue.popleft()

                #right
                if check_and_push(i, min(j+1, len(grid[0]) - 1), visited):
                    res += 1
                #down
                if check_and_push(min(i+1, len(grid)-1), j, visited):
                    res += 1
                #left
                if check_and_push(i, max(0, j-1), visited):
                    res += 1
                #up
                if check_and_push(max(0, i-1), j, visited):
                    res += 1

            queue = tmp

        return res
