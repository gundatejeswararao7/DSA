
"""
14. Longest Common Prefix
Difficulty: Easy
Topic: Array, String
Link: https://leetcode.com/problems/longest-common-prefix/

Approach:
    If the input list is empty, return an empty string. Find the shortest
    string because the common prefix cannot be longer than it. Iterate
    through each character of the shortest string and compare it with
    the character at the same position in every string. If a mismatch
    occurs, return the substring before that position. If no mismatch
    occurs, return the entire shortest string.

Complexity:
    Time:  O(n * m)
    Space: O(1) auxiliary space

    Here, n is the number of strings and m is the length of the
    shortest string.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_str = strs[0]

        for s in strs:
            if len(s) < len(min_str):
                min_str = s

        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[:i]

        return min_str
