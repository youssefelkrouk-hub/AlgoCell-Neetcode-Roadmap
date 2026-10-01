from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        rs = []
        top, bottom, left, right = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            # Top Traversal
            for i in range(left, right + 1):
                rs.append(matrix[top][i])
            # Left Traversal
            for i in range(top + 1, bottom):
                rs.append(matrix[i][right])
            # Bottom Traversal
            if bottom != top:
                for i in range(right, left - 1, -1):
                    rs.append(matrix[bottom][i])
            # Right Traversal
            if left != right:
                for i in range(bottom - 1, top, -1):
                    rs.append(matrix[i][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return rs
