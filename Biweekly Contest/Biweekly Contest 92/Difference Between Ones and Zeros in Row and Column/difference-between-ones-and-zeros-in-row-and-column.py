class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        grl = len(grid)
        gcl = len(grid[0])
        
        diff = [ [0] * gcl for _ in range(grl)]
        
        rows = {}
        cols = {}
        
        for i, r in enumerate(grid):
            rows[i] = sum(r)
        
        grid = list(map(list, zip(*grid)))
        
        for i, c in enumerate(grid):
            cols[i] = sum(c)
            
        for i in range(grl):
            for j in range(gcl):
                diff[i][j] = rows[i] + cols[j] - (gcl - rows[i]) - (grl - (cols[j]))
    
        return diff
