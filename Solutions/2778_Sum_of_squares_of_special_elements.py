"""
2778. Sum of Squares of Special Elements
Difficulty: Easy
Topic: Array, Math
Link: https://leetcode.com/problems/sum-of-squares-of-special-elements/

Approach:
    Find the length n of the array and iterate through indices from
    1 to n. If n is divisible by the current index i, the element
    nums[i - 1] is a special element. Add its square to the result
    and return the final sum.

Complexity:
    Time:  O(n)
    Space: O(1)
"""

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        add = 0
        n = len(nums)

        for i in range(1, n + 1):
            if n % i == 0:
                add += nums[i - 1] * nums[i - 1]

        return add