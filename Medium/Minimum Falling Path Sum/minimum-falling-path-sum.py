class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                a = matrix[i-1][j]
                b = matrix[i-1][max(0, j-1)]
                c = matrix[i-1][min(j+1, len(matrix[0]) - 1)]

                matrix[i][j] += min(a, b, c)

        return min(matrix[-1])
