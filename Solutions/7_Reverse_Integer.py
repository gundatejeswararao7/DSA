"""
7. Reverse Integer
Difficulty: Medium
Topic: Math
Link: https://leetcode.com/problems/reverse-integer/

Approach:
    Check whether the integer is negative. If so, convert it to positive
    and store its sign using a flag. Extract the last digit using x % 10
    and build the reversed number by multiplying the result by 10 and
    adding the digit. Remove the last digit using x //= 10. Restore the
    negative sign if needed. Finally, check whether the reversed number
    falls within the signed 32-bit integer range. If it overflows, return 0.

Complexity:
    Time:  O(log |x|)
    Space: O(1)
"""

class Solution:
    def reverse(self, x: int) -> int:
        found = False

        if x < 0:
            x = -x
            found = True

        place = 0

        while x != 0:
            rem = x % 10
            place = place * 10 + rem
            x //= 10

        if found:
            place = -place

        # Check for 32-bit integer overflow
        if place < -2**31 or place > 2**31 - 1:
            return 0

        return place
