class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        res = []
        
        for col in range(len(grid[0])):
            stucked = False
            for row in range(len(grid)):
                
                if (
                    col == 0 and grid[row][col] == -1
                ) or (
                    col == len(grid[0]) - 1 and grid[row][col] == 1
                ):
                    stucked = True
                    break
                    
                curr_col = col
                col += grid[row][col]
                
                if grid[row][curr_col] != grid[row][col]:
                    stucked = True
                    break
                
            res.append(col if not stucked else -1)

        return res
