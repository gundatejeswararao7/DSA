"""
17. Letter Combinations of a Phone Number
Difficulty: Medium
Topic: String, Backtracking, Recursion
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Approach:
    Create a phone dictionary that maps each digit to its letters.
    Use backtracking to build combinations one character at a time.
    At each index, iterate through the letters corresponding to the
    current digit and recursively explore each choice.
    When the path length equals the digits length, join the characters
    and add the combination to the result.
    Return an empty list if digits is empty.

Complexity:
    Time:  O(4^n * n), where n is the length of digits
    Space: O(n) auxiliary space for recursion, excluding output
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return

            for ch in phone[digits[i]]:
                backtrack(i + 1, path + [ch])

        backtrack(0, [])
        return res
