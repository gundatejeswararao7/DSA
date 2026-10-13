"""
9. Palindrome Number
Difficulty: Easy
Topic: Math, Two Pointers, String
Link: https://leetcode.com/problems/palindrome-number/

Approach:
    Convert the integer into a string. Use two pointers, l at the
    beginning and r at the end. Compare the characters at both
    positions. If they differ, return False. Otherwise, move l
    forward and r backward until they meet. If all corresponding
    characters match, return True.

Complexity:
    Time:  O(n)
    Space: O(n)
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
