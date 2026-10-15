
"""
16. 3Sum Closest
Difficulty: Medium
Topic: Array, Two Pointers, Sorting
Link: https://leetcode.com/problems/3sum-closest/

Approach:
    Sort the array and fix each element nums[i]. Use two pointers,
    left and right, to find a triplet sum. Calculate the absolute
    difference between the sum and the target. If the difference
    is smaller than min_diff, update min_diff and closest_sum.
    If the sum is less than the target, move left forward to increase
    the sum; otherwise, move right backward to decrease it.
    Return the closest sum after checking all possible triplets.

Complexity:
    Time:  O(n^2)
    Space: O(1) auxiliary space, excluding sorting
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        closest_sum = 0
        n = len(nums)

        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                diff = abs(val - target)

                if diff < min_diff:
                    min_diff = diff
                    closest_sum = val

                if val < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum
