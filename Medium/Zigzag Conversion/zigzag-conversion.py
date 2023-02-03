class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[0] * len(s) for i in range(numRows)]
        row, col = -1, -1

        for c in s:
            row = (row + 1) % numRows
            col = col + 1 if row == 0 else col
            if col % numRows != 0:
                row = numRows - (col % numRows) - 1
                matrix[row][col] = c
                col += 1
                continue

            matrix[row][col] = c

        res = ""

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    res += matrix[i][j]

        return res
