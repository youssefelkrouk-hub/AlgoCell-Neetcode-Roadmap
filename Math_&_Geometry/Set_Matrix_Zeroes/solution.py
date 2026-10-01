from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row = False
        col = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    if i == 0:
                        row = True
                    if j == 0:
                        col = True

        for i in range(n - 1, 0, -1):
            for j in range(m - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row:
            for i in range(m):
                matrix[0][i] = 0
        if col:
            for i in range(n):
                matrix[i][0] = 0
