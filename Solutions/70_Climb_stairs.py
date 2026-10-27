"""
70. Climbing Stairs
Difficulty: Easy
Topic: Dynamic Programming, Recursion, Memoization
Link: https://leetcode.com/problems/climbing-stairs/

Approach:
    Use recursion with memoization to avoid repeated calculations.
    Initialize memo with {0: 1, 1: 1}, representing one way to climb
    zero or one step.
    For each n, calculate the number of ways as the sum of ways to
    climb n-1 and n-2 steps.
    Store each result in memo and return fiba(n).

Complexity:
    Time:  O(n), because each state is calculated once
    Space: O(n) for the memoization dictionary and recursion stack
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def fiba(n):
            if n in memo:
                return memo[n]

            memo[n] = fiba(n - 1) + fiba(n - 2)
            return memo[n]

        return fiba(n)
