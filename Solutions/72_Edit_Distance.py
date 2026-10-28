"""
72. Edit Distance
Difficulty: Medium
Topic: String, Dynamic Programming
Link: https://leetcode.com/problems/edit-distance/

Approach:
    Create a DP table of size (m+1) x (n+1), where dp[i][j] represents
    the minimum operations needed to convert the first i characters
    of word1 into the first j characters of word2.
    Initialize the first row and column to handle empty strings.
    If the current characters match, use dp[i-1][j-1].
    Otherwise, consider three operations:
        Insert:  dp[i][j-1]
        Delete:  dp[i-1][j]
        Replace: dp[i-1][j-1]
    Add 1 to the minimum of these three values.
    Return dp[m][n].

Complexity:
    Time:  O(m * n)
    Space: O(m * n) for the DP table
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for col in range(n + 1):
            dp[0][col] = col

        for row in range(m + 1):
            dp[row][0] = row

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1]
                    )

        return dp[m][n]
