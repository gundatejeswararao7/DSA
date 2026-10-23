"""
45. Jump Game II
Difficulty: Medium
Topic: Array, Greedy
Link: https://leetcode.com/problems/jump-game-ii/

Approach:
    Use a greedy approach with three variables:
    jumps: number of jumps made so far.
    curr: farthest index reachable using the current number of jumps.
    far: farthest index reachable by exploring the current range.

    Traverse the array up to the second-last index and update far
    using i + nums[i].
    When i reaches curr, increment jumps and update curr = far.
    This means we must take another jump to continue progressing.
    Return jumps as the minimum number of jumps needed to reach the end.

Complexity:
    Time:  O(n), where n is the length of nums
    Space: O(1) auxiliary space
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = curr = far = 0

        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])

            if i == curr:
                jumps += 1
                curr = far

        return jumps
