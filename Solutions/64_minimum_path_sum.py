"""
64. Minimum Path Sum
Difficulty: Medium
Topic: Array, Dynamic Programming, Matrix
Link: https://leetcode.com/problems/minimum-path-sum/

Approach:
    Create an m x n DP table to store the minimum path sum to reach
    each cell.
    Initialize the first cell with grid[0][0].
    Fill the first row by adding the current cell to the left cell's sum.
    Fill the first column by adding the current cell to the upper cell's sum.
    For every remaining cell, add its value to the minimum of the sums
    from the left and above.
    Return result[m-1][n-1] as the minimum path sum.

Complexity:
    Time:  O(m * n)
    Space: O(m * n) for the DP table
"""

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        result = [[0] * n for _ in range(m)]

        result[0][0] = grid[0][0]

        for col in range(1, n):
            result[0][col] = result[0][col - 1] + grid[0][col]

        for row in range(1, m):
            result[row][0] = result[row - 1][0] + grid[row][0]

        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = grid[i][j] + min(
                    result[i][j - 1],
                    result[i - 1][j]
                )

        return result[m - 1][n - 1]
