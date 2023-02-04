class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        
        xl, yl = len(grid), len(grid[0])

        res = [0] * (xl + yl - 1)

        for i in range(xl):
            for j in range(yl):
                if grid[i][j] == 1:
                    res[i+j] += 1

        for n in res[1:-1]:
            if n < 2:
                return True

        return False
