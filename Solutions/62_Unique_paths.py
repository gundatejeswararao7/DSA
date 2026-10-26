"""
62. Unique Paths
Difficulty: Medium
Topic: Array, Dynamic Programming, Matrix
Link: https://leetcode.com/problems/unique-paths/

Approach:
    Create an m x n DP table initialized with zeros.
    Set the first row and first column to 1 because there is only
    one way to reach any cell in the first row or first column.
    For every remaining cell, calculate the number of paths by adding
    the paths from the cell above and the cell to the left.
    Return dp[m-1][n-1] as the total number of unique paths.

Complexity:
    Time:  O(m * n)
    Space: O(m * n) for the DP table
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        for row in range(m):
            dp[row][0] = 1

        for col in range(n):
            dp[0][col] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]
