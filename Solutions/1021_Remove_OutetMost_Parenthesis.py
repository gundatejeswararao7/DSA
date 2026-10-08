
"""
1021. Remove Outermost Parentheses
Difficulty: Easy
Topic: Stack, String
Link: https://leetcode.com/problems/remove-outermost-parentheses/

Approach:
    Use a balance counter to track the nesting depth of parentheses.
    When encountering '(', append it only if the balance is greater
    than 0, then increase the balance. When encountering ')', decrease
    the balance first and append it only if the balance is greater
    than 0. This skips the outermost parentheses of each primitive
    valid parentheses string.

Complexity:
    Time:  O(n)
    Space: O(n)
"""

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        bal = 0

        for c in s:
            if c == '(':
                if bal > 0:
                    res.append(c)
                bal += 1
            else:
                bal -= 1
                if bal > 0:
                    res.append(c)

        return ''.join(res)
