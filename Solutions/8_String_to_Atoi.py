"""
8. String to Integer (atoi)
Difficulty: Medium
Topic: String
Link: https://leetcode.com/problems/string-to-integer-atoi/

Approach:
    Remove leading and trailing whitespace using strip(). If the string
    is empty, return 0. Check the first character for '+' or '-' to
    determine the sign. Iterate through the remaining characters and
    build the integer digit by digit until a non-digit character appears.
    Apply the sign and clamp the result to the signed 32-bit integer
    range: [-2^31, 2^31 - 1].

Complexity:
    Time:  O(n)
    Space: O(n)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        place = 0
        found = False
        i = 0

        if s[0] == "-":
            found = True
            i = 1
        elif s[0] == "+":
            i = 1

        for i in range(i, len(s)):
            if s[i].isdigit():
                place = place * 10 + int(s[i])
            else:
                break

        if found:
            place = -place

        if place > 2**31 - 1:
            return 2**31 - 1

        if place < -2**31:
            return -2**31

        return place
