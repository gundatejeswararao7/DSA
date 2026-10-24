"""
54. Spiral Matrix
Difficulty: Medium
Topic: Array, Matrix, Simulation
Link: https://leetcode.com/problems/spiral-matrix/

Approach:
    Use four boundaries to track the remaining unvisited portion
    of the matrix: left, right, top, and bottom.

    Traverse the matrix in spiral order:
        1. Left to right across the top row.
        2. Top to bottom along the right column.
        3. Right to left across the bottom row, if rows remain.
        4. Bottom to top along the left column, if columns remain.

    After traversing each boundary, move it inward to avoid
    revisiting elements.

    Continue until the boundaries cross, then return the result.

Complexity:
    Time:  O(m * n)  # Visit each element exactly once
    Space: O(1)       # Auxiliary space, excluding the output list
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nums = []
        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            # Traverse from left to right
            for i in range(left, right + 1):
                nums.append(matrix[top][i])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                nums.append(matrix[i][right])
            right -= 1

            # Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    nums.append(matrix[bottom][i])
                bottom -= 1

            # Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    nums.append(matrix[i][left])
                left += 1

        return nums
