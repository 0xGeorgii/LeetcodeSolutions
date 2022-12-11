class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        
        res = 0
        for r in grid: r.sort(reverse=True)
        for _ in range(len(grid[0])): 
            r = 0           
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 0:
                        continue
                    r = max(r, grid[i][j])
                    grid[i][j] = 0
                    break
            res += r
            
        
        return res
