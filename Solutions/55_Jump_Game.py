"""
55. Jump Game
Difficulty: Medium
Topic: Array, Greedy
Link: https://leetcode.com/problems/jump-game/

Approach:
    Use a greedy approach to track the farthest index that
    can be reached so far.

    Initialize max_reach to 0 and goal to the last index.

    Iterate through each index:
        1. If the current index is greater than max_reach,
           return False because it cannot be reached.
        2. Update max_reach to the maximum of its current value
           and i + nums[i].
        3. If max_reach reaches or exceeds the goal, return True.

    If the last index is unreachable, return False.

Complexity:
    Time:  O(n)  # Visit each element at most once
    Space: O(1)  # Use only a constant amount of extra space
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        goal = len(nums) - 1

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= goal:
                return True

        return False
