class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        res = []
        
        for col in range(len(grid[0])):
            next_col = col
            stucked = False
            for row in range(len(grid)):
                
                if (
                    next_col == 0 and grid[row][next_col] == -1
                ) or (
                    next_col == len(grid[0]) - 1 and grid[row][next_col] == 1
                ):
                    stucked = True
                    break
                    
                curr_col = next_col
                next_col += grid[row][next_col]
                
                if grid[row][curr_col] != grid[row][next_col]:
                    stucked = True
                    breaka
                
            res.append(next_col if not stucked else -1)

        return res
