"""
73. Set Matrix Zeroes
Difficulty: Medium
Topic: Array, Matrix
Link: https://leetcode.com/problems/set-matrix-zeroes/

Approach:
    First, use zeros_place() to collect the positions of all original
    zeros in the matrix.
    Then, for each recorded position, set every element in its row and
    column to zero by moving left, right, up, and down.
    Store the original zero positions before modifying the matrix so
    newly created zeros do not affect which rows and columns are processed.
    The matrix is modified in place.

Complexity:
    Time:  O(m * n + z * (m + n)), where z is the number of original zeros
    Space: O(z) for storing the original zero positions
"""

from typing import List

class Solution:
    def zeros_place(self, matrix, rows, cols):
        zeros_list = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeros_list.append((i, j))

        return zeros_list

    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        rows = len(matrix)
        cols = len(matrix[0])
        zeros = self.zeros_place(matrix, rows, cols)

        index = 0

        while index < len(zeros):
            r, c = zeros[index]

            # Move left in the row
            temp_c = c
            while temp_c >= 0:
                matrix[r][temp_c] = 0
                temp_c -= 1

            # Move right in the row
            temp_c = c
            while temp_c < cols:
                matrix[r][temp_c] = 0
                temp_c += 1

            # Move up in the column
            temp_r = r
            while temp_r >= 0:
                matrix[temp_r][c] = 0
                temp_r -= 1

            # Move down in the column
            temp_r = r
            while temp_r < rows:
                matrix[temp_r][c] = 0
                temp_r += 1

            index += 1
