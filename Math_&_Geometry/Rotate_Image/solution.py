from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = 0
        r = len(matrix) - 1
        while l < r:
            for i in range(r - l):
                topLeft = matrix[l][l + i]
                matrix[l][l + i] = matrix[r - i][l]
                matrix[r - i][l] = matrix[r][r - i]
                matrix[r][r - i] = matrix[l + i][r]
                matrix[l + i][r] = topLeft
            l += 1
            r -= 1
