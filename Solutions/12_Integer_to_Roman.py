
"""
12. Integer to Roman
Difficulty: Medium
Topic: Hash Table, Math, String, Greedy
Link: https://leetcode.com/problems/integer-to-roman/

Approach:
    Store Roman numeral symbols and their corresponding integer values
    in descending order. Iterate through the dictionary and find the
    largest value that is less than or equal to num. Append its Roman
    symbol to result and subtract its value from num. Repeat until num
    becomes 0. This greedy approach builds the Roman numeral from
    largest to smallest, including subtractive forms such as CM, CD,
    XC, XL, IX, and IV.

Complexity:
    Time:  O(1)
    Space: O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        roman = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }

        while num != 0:
            for key, value in roman.items():
                if num >= value:
                    result += key
                    num -= value
                    break

        return result
