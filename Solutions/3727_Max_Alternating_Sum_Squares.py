"""
1911. Maximum Alternating Subsequence Sum
Difficulty: Medium
Topic: Array, Sorting, Greedy
Link: https://leetcode.com/problems/maximum-alternating-subsequence-sum/

Approach:
    Square every element in nums and sort the squared values in ascending
    order. Divide the sorted array into two parts using k = n // 2.
    Subtract the sum of the smaller half from the sum of the larger half
    to maximize the alternating sum.

Complexity:
    Time:  O(n log n)
    Space: O(n)
"""

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a = sorted(x * x for x in nums)

        k = len(nums) // 2
        return sum(a[k:]) - sum(a[:k])
