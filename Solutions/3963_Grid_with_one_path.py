"""
Create Grid
Difficulty: Easy
Topic: Array, Matrix, Simulation
Link: Custom function / no confirmed LeetCode problem link

Approach:
    Create an m x n grid filled with '#'.
    Replace every cell in the first row with '.'.
    Replace every cell in the last column with '.'.
    Convert each row into a string and return the list of strings.

Complexity:
    Time:  O(m * n)
    Space: O(m * n) for the grid and output
"""

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        for j in range(n):
            grid[0][j] = '.'

        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]
