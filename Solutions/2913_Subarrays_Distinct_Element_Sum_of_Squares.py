
"""
Sum of Squares of Distinct Counts
Difficulty: Medium
Topic: Array, Hash Set, Sliding Window
Link: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

Approach:
    Consider every possible starting index of a subarray. Use a set
    to track distinct elements while extending the subarray to the
    right. For each extension, calculate the square of the number
    of distinct elements and add it to the result. Return the total
    after processing all subarrays.

Complexity:
    Time:  O(n^2)
    Space: O(n)
"""

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                res += len(distinct) ** 2

        return res
