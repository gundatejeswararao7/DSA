"""
18. 4Sum
Difficulty: Medium
Topic: Array, Two Pointers, Sorting
Link: https://leetcode.com/problems/4sum/

Approach:
    Sort the array to make it easier to find quadruplets using two pointers.
    Use two nested loops to select the first two elements, nums[i] and nums[j].
    Skip duplicate values for i and j to avoid duplicate quadruplets.
    Use left and right pointers to find the remaining two elements.
    If the total equals the target, add the quadruplet to the result and
    skip duplicate values by moving both pointers.
    If the total is less than the target, move left forward; otherwise,
    move right backward.
    Return all unique quadruplets.

Complexity:
    Time:  O(n^3)
    Space: O(1) auxiliary space, excluding sorting and output
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[i], nums[j], nums[left], nums[right]
                        ])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
