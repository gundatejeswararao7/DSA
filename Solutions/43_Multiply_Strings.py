"""
43. Multiply Strings
Difficulty: Medium
Topic: String, Math, Simulation
Link: https://leetcode.com/problems/multiply-strings/

Approach:
    Convert each numeric string into an integer manually using place values.
    Traverse each string from right to left, multiply each digit by its
    place value, and add it to the result.
    Multiply the two converted integers and return the product as a string.

    Note: This approach is simple, but LeetCode expects multiplication
    without directly converting the entire strings into integers.

Complexity:
    Time:  O(n + m), excluding the multiplication cost of large integers
    Space: O(1) auxiliary space, excluding integer storage
"""

class Solution:
    def StringToInteger(self, num: str) -> int:
        place = 1
        n = 0

        for i in range(len(num) - 1, -1, -1):
            n += place * int(num[i])
            place *= 10

        return n

    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.StringToInteger(num1)
        num2 = self.StringToInteger(num2)

        return str(num1 * num2)
