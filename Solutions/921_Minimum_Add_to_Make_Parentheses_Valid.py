"""
921. Minimum Add to Make Parentheses Valid
Difficulty: Medium
Topic: Stack
Link: https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

Approach:
    Use a stack to keep track of unmatched opening parentheses.
    For every '(' push it into the stack. For every ')', if there is
    an unmatched '(', remove it from the stack; otherwise, this ')'
    needs an extra '(' so increment res. At the end, the remaining
    opening parentheses in the stack each need an extra ')'.

Complexity:
    Time:  O(n)
    Space: O(n)
"""

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        res = 0

        for i in s:
            if i == '(':
                stack.append(i)

            elif len(stack) > 0 and i == ')':
                stack.pop()

            elif i == ')':
                res += 1

        return len(stack) + res
