class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        cl = len(matrix[0])
        if cl == 1:
            return len(matrix)
        
        res = 0
        for c in itertools.combinations(range(cl), numSelect):
            nr = 0
            for i in range(len(matrix)):
                if sum(matrix[i]) == 0:
                    nr += 1
                    continue
                for j in range(cl):
                  if matrix[i][j] == 1 and j not in c:
                    break
                else:
                    nr += 1
            
            res = max(res, nr)
        
        return res
