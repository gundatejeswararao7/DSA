"""
53. Maximum Subarray
Difficulty: Medium
Topic: Array, Dynamic Programming, Greedy, Kadane's Algorithm
Link: https://leetcode.com/problems/maximum-subarray/

Approach:
    Use Kadane's Algorithm to find the maximum sum of a contiguous subarray.
    Initialize curr_sum and max_sum with the first element.
    Traverse the remaining elements and choose between starting a new
    subarray at the current element or extending the existing subarray.
    Update max_sum whenever a larger sum is found.
    Return max_sum. Handle an empty array by returning 0.

Complexity:
    Time:  O(n), where n is the length of nums
    Space: O(1) auxiliary space
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = nums[0]
        curr_sum = nums[0]

        for curr_ele in nums[1:]:
            curr_sum = max(curr_ele, curr_sum + curr_ele)
            max_sum = max(max_sum, curr_sum)

        return max_sum
