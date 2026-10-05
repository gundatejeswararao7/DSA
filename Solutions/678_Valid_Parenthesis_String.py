"""
678. Valid Parenthesis String
Difficulty: Medium
Topic: Stack, Dynamic Programming, Top-Down Approach
Link: https://leetcode.com/problems/valid-parenthesis-string/

Approach:
    Use Top-Down Dynamic Programming with memoization.
    At each index, keep track of the current parenthesis balance.
    '(' increases the balance, ')' decreases it, and '*' can be treated
    as '(', ')' or an empty string. If the balance becomes negative,
    the string cannot be valid. At the end, the balance must be 0.
    Store each (index, balance) result in memo to avoid recalculating
    the same state.

Complexity:
    Time:  O(n^2)
    Space: O(n^2)
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def solve(i, balance):
            # Too many closing parentheses
            if balance < 0:
                return False

            # End of string
            if i == len(s):
                return balance == 0

            # Already calculated
            if (i, balance) in memo:
                return memo[(i, balance)]

            if s[i] == '(':
                result = solve(i + 1, balance + 1)

            elif s[i] == ')':
                result = solve(i + 1, balance - 1)

            else:  # '*'
                result = (
                    solve(i + 1, balance + 1) or  # '*' -> '('
                    solve(i + 1, balance - 1) or  # '*' -> ')'
                    solve(i + 1, balance)         # '*' -> ''
                )

            memo[(i, balance)] = result
            return result

        return solve(0, 0)
