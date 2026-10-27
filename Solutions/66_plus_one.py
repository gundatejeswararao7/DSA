"""
66. Plus One
Difficulty: Easy
Topic: Array, Math
Link: https://leetcode.com/problems/plus-one/

Approach:
    Initialize carry = 1 because we need to add one to the number.
    Traverse the digits from right to left and add the carry to each digit.
    If a digit becomes greater than 9, set it to 0 and keep carry = 1.
    Otherwise, set carry = 0 and stop because no further changes are needed.
    If carry is still 1 after processing all digits, insert 1 at the beginning.
    Return the updated digits list.

Complexity:
    Time:  O(n), where n is the number of digits
    Space: O(1) auxiliary space, excluding the possible extra digit
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry

            if digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
                break

        if carry == 1:
            digits.insert(0, 1)

        return digits
